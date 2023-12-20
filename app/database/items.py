from typing import List
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.Item import ItemCreate
from app.services.tasks import process_item

def create_item(db: Session, item: ItemCreate, user_id: int, background_tasks: BackgroundTasks):
    db_item = Item(name = item.name, quantity = item.quantity, customer_id = user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    background_tasks.add_task(process_item, db, item_id=db_item.id)
    return db_item

def get_items_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> List[Item]:
    return db.query(Item).filter(Item.customer_id == user_id).order_by(Item.name).offset(skip).limit(limit).all()


