from typing import List
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.items import create_item, get_items_by_user_id
from app.dependencies.auth import get_current_user
from app.schemas import User
from app.schemas.Item import ItemCreate, Item

router = APIRouter()

@router.post("/items/", response_model=ItemCreate)
def items(item: ItemCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print(current_user)
    db_item = create_item(db, item, user_id=current_user.id, background_tasks=background_tasks)
    return ItemCreate(name=db_item.name, quantity=db_item.quantity)

@router.get("/items/", response_model=List[Item])
def read_user_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    items = get_items_by_user_id(db, user_id=current_user.id, skip=skip, limit=limit)
    return [Item(name=x.name, quantity=x.quantity, reservation_id=x.reservation_id) for x in items]