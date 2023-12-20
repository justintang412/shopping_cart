from typing import Optional
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    quantity: int
    
class Item(BaseModel):
    name: str
    quantity: int
    reservation_id: Optional[str]
    

class ItemReservationId(BaseModel):
    id: int
    reservation_id: str
