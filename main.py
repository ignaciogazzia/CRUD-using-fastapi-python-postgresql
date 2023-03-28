from fastapi import FastAPI
from BusinessLogic.Product import *

app = FastAPI()


@app.get('/')
def read_root():
    return {"greeting": "Welcome to my first API for Products and Packages!"}


@app.get('/products')
async def get_products():
    return show_all_products()


@app.get('/products/{product_id}')
async def get_product_by_id(product_id: int):
    return show_product_by_id(product_id)


@app.post('/products')
async def new_product(product: Product):
    return create_product(product)


@app.put('/products/{product_id}')
async def update_product(product_id: int, product_updates: Product):
    return update_product_by_id(product_id, product_updates)


@app.put('/products/{product_id}')
async def activate_deactivate_product(product_id: int):
    return update_is_active(product_id)
