from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.database import Base
from app.models.user import User
from app.models.item import Item
from werkzeug.security import generate_password_hash

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create some sample users
    db = SessionLocal()
    try:
        user1 = User(username="user1", email="user1@example.com",
                     full_name="User One", hashed_password=generate_password_hash('password1'))
        user2 = User(username="user2", email="user2@example.com",
                     full_name="User Two", hashed_password=generate_password_hash('password2'))

        db.add(user1)
        db.add(user2)
        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    init_db()
    print("Database tables created.")
