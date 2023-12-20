from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.database import SQLALCHEMY_DATABASE_URL, Base
from app.database.items import get_items_by_user_id
from app.models.user import User
from app.models.item import Item

from werkzeug.security import generate_password_hash

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def setup_module():
    # Set up the test database and create tables
    Base.metadata.create_all(bind=engine)

def teardown_module():
    # Clean up the test database
    Base.metadata.drop_all(bind=engine)

def test_get_user_with_items():
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

    items = get_items_by_user_id(db, user_id=user.id)

    assert items is not None
    assert len(items) == 2
    assert items[0].name == "Item 1"
    assert items[1].name == "Item 2"
