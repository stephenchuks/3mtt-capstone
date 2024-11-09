from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product

router = APIRouter()

@router.post("/products/")
def create_product(name: str, price: int, stock: int, db: Session = Depends(get_db)):
    new_product = Product(name=name, price=price, stock=stock)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/products/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": "Sample Product"}

