from sqlalchemy import Column, Integer, String
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)

