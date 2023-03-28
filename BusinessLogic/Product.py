import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Client(SQLModel, table=True):
    client_id: Optional[int] = Field(default=None, primary_key=True)
    client_name: str = Field(index=True)
    is_active: bool
    country_id: int
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None


class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)  # Mandatory
    price: int  # Mandatory
    is_active: bool  # Mandatory
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None


DATABASE_NAME = 'Personas'
DATABASE_URL = f'postgresql://postgres:igna+1234@localhost:5432/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_product(new_product: Product):
    new_product = Product(title=new_product.title, price=new_product.price, created_at=datetime.datetime.now())
    with Session(engine) as session:
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
    return new_product


def show_all_products():
    with Session(engine) as session:
        return session.exec(select(Product)).all()


def show_product_by_id(product_id):
    with Session(engine) as session:
        return session.exec(select(Product).where(Product.product_id == product_id)).all()
    # Si no lo encuentra, devuelve None


def update_product_by_id(product_id, product_updates: Product):
    with Session(engine) as session:
        product_to_update = session.exec(select(Product).where(Product.product_id == product_id)).first()
        if product_to_update is not None:
            product_to_update.title = product_updates.title
            product_to_update.price = product_updates.price
            product_to_update.is_active = product_updates.is_active
            product_to_update.updated_at = datetime.datetime.now()
            session.add(product_to_update)
            session.commit()
            session.refresh(product_to_update)
        return product_to_update


def update_is_active(product_id: int):
    with Session(engine) as session:
        prod_to_delete = session.exec(select(Product).where(Product.product_id == product_id)).first()
        if prod_to_delete.is_active:
            prod_to_delete.is_active = False
        else:
            prod_to_delete.is_active = True
        prod_to_delete.updated_at = datetime.datetime.now()
        session.add(prod_to_delete)
        session.commit()
        session.refresh(prod_to_delete)
    return prod_to_delete


if __name__ == "__main__":
    pass
