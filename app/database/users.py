from sqlalchemy.orm import Session,joinedload
from app.models.user import User

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).options(joinedload(User.items)).first()
