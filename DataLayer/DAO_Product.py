from Services.DBConnection import DBConnection
from BusinessLogic.Product import *
from logger import log


class ProductDAO:
    _SELECT = 'SELECT * FROM public."Product" ORDER BY product_id'
    _INSERT = 'INSERT INTO public."Product"(title, created_at) VALUES(%s, now())'
    _UPDATE = 'UPDATE public."Product" SET title=%s, updated_at=now() WHERE product_id=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona=%s'
    _SELECT_ONE_BY_ID = 'SELECT * FROM public."Product" WHERE product_id=%s'

    @classmethod
    def show_products(cls):
        with DBConnection.get_cursor() as cursor:
            cursor.execute(cls._SELECT)
            products = cursor.fetchall()
            return [Product(product[0], product[1], product[2]) for product in products]

    @classmethod
    def show_product(cls, product_id):
        with DBConnection.get_cursor() as cursor:
            cursor.execute(cls._SELECT_ONE_BY_ID, (product_id,))
            product = cursor.fetchone()
            if product is not None:
                return Product(product_id=product[0], title=product[1], created_at=product[2])
            return None


    @classmethod
    def insert_product(cls, product_to_insert):
        with DBConnection.get_cursor() as cursor:
            # insert_params = product.title
            cursor.execute(cls._INSERT, (product_to_insert.title,))
            log.debug(f'Product inserted: {product_to_insert}')
            DBConnection.commit()

    @classmethod
    def update_product(cls, product_id, new_title):
        with DBConnection.get_cursor() as cursor:
            if ProductDAO.product_exists(product_id, cursor):
                cursor.execute(cls._UPDATE, (new_title, product_id))
                cursor.execute(cls._SELECT_ONE_BY_ID, (product_id,))
                product_updated = cursor.fetchone()
                DBConnection.commit()
                log.debug(f'Product updated: {product_id}')
                return Producto.to_dict(product_updated)
            else:
                log.debug(f'Product you\'re trying to update doesnt exist: {product_id}')
                return {}

    @classmethod
    def product_exists(cls, product_id, cursor) -> bool:
        exists = False
        cursor.execute(cls._SELECT_ONE_BY_ID, (product_id,))
        if cursor.fetchone() is not None:
            exists = True
        return exists



if __name__ == '__main__':
    product = ProductDAO.update_product(15,"Taza de Chocolate")
    print(product)
