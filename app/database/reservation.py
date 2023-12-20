from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.Item import ItemReservationId

def update_reservation_id(db: Session, item: ItemReservationId):
    db_item = db.query(Item).filter(Item.id == item.id).first()
    if db_item:
        db_item.reservation_id = item.reservation_id
        db.commit()

    return db_item
