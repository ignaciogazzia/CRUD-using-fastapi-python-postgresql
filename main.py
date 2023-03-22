from fastapi import FastAPI
from DataLayer.DAO_Product import ProductDAO

app = FastAPI()


@app.get('/')
def read_root():
    return {"greeting": "Welcome to my first API for Products and Packages!"}


@app.get('/products')
async def get_products():
    products = ProductDAO.show_products()
    return [product.to_dict() for product in products]


@app.get('/products/{product_id}')
async def get_product_by_id(product_id: int):
    product = ProductDAO.show_product(product_id)
    if product is None:
        return {}
    return product.to_dict()

