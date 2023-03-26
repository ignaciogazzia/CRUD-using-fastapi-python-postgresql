import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    created_at: datetime.datetime | None = None


DATABASE_NAME = 'Personas'
DATABASE_URL = f'postgresql://postgres:admin@localhost:5432/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_product(product_title: str):
    new_product = Product(title=product_title, created_at=datetime.datetime.now())
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



if __name__ == "__main__":
    # create_db_and_tables()
    # create_product('Caja de aluminio')
    producto = show_product_by_id(2)
    print(producto)
