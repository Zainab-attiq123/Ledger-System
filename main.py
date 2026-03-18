from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from auth import login

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Login
@app.post("/login")
def user_login(username: str, password: str):
    return login(username, password)

# Add Customer
@app.post("/customers")
def add_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

# Add Product
@app.post("/products")
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

# Transaction (Debit / Credit)
@app.post("/transactions")
def transaction(txn: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, txn)