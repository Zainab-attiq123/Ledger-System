from sqlalchemy.orm import Session
import models

def create_customer(db: Session, customer):
    db_customer = models.Customer(name=customer.name, phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_product(db: Session, product):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_transaction(db: Session, txn):
    customer = db.query(models.Customer).filter(models.Customer.id == txn.customer_id).first()

    if txn.type == "debit":
        customer.balance += txn.amount
    else:
        customer.balance -= txn.amount

    db_txn = models.Transaction(**txn.dict())
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)

    return db_txn