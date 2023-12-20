from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from app.main import app
from app.database.database import SQLALCHEMY_DATABASE_URL, Base
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.models.item import Item
from werkzeug.security import generate_password_hash


engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def setup_module():
    # Set up the test database and create tables
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    # Create a test user and items
    db = TestingSessionLocal()
    user = User(username="testuser", email="test@example.com", full_name="Test User",hashed_password=generate_password_hash('password1'))

    db.add(user)
    db.commit()
    item1 = Item(name="Item 1", quantity=1, customer_id=user.id)
    item2 = Item(name="Item 2", quantity=1, customer_id=user.id)
    db.add(item1)
    db.add(item2)
    db.commit()


def teardown_module():
    # Clean up the test database
    Base.metadata.drop_all(bind=engine)


def test_routes():
    client = TestClient(app)
    
    response_auth = client.post(
        "/token", data={"username": "testuser", "password": "password1"})
    assert response_auth.status_code == 200
    jwt_token = response_auth.json()["access_token"]
    headers = {"Authorization": f"Bearer {jwt_token}"}
    response = client.post("/items/", json={
        "name": "apple",
        "quantity": 1
    }, headers=headers)
    assert response.status_code == 200
    response = client.get("/items/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 3
    
    
