from sqlalchemy import Column, ForeignKey, Integer, String
from app.database.database import Base
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, default=0)
    reservation_id = Column(String, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="items")