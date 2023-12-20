from app.database.reservation import update_reservation_id
from app.schemas.Item import ItemReservationId
from sqlalchemy.orm import Session

def process_item(db: Session, item_id: int):
    # import time
    # time.sleep(30)
    
    reservation_id = "some_reservation_id"
    update_reservation_id(db, ItemReservationId(id=item_id, reservation_id=reservation_id))

    print(f"Background task completed for Item ID {item_id}. Reservation ID updated to {reservation_id}")
