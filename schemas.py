from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    phone: str

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class TransactionCreate(BaseModel):
    customer_id: int
    amount: float
    type: str