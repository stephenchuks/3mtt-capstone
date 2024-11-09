from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order

router = APIRouter()

@router.post("/orders/")
def create_order(item_name: str, quantity: int, customer_id: int, db: Session = Depends(get_db)):
    new_order = Order(item_name=item_name, quantity=quantity, customer_id=customer_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/orders/{order_id}")
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return i{"order": "Sample Order"}

