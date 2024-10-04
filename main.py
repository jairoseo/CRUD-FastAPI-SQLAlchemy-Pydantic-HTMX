from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from router_frontend import router
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#FRONTEND
app.include_router(router)

#BACKEND
@app.post("/product/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/product/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_product

@app.put("/product/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db, product_id=product_id, product=product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_product

@app.delete("/product/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    else:
        return {'mensaje': 'Producto Borrado'}