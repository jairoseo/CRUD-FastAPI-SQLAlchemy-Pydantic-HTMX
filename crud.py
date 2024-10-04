from sqlalchemy.orm import Session
import models, schemas

def get_product(db: Session, product_id : int):
    return db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit : int = 0):
    return db.query(models.ProductModel).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id : int, product: schemas.ProductUpdate):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()
    if not db_product:
        db_product = False
    else:
        for key, value in product.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
    return db_product

def delete_product(db: Session, product_id : int):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()
    if not db_product:
        db_product = False
    else:
        db.delete(db_product)
        db.commit()
    return db_product