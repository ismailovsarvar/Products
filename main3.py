# class Product:
#     db_name = 'products.db'
#
#     def __init__(self, id, name, price):
#         self.id = id
#         self.name = name
#         self.price = price
#
#     @classmethod
#     def create_table(cls):
#         with ConnectDb(cls.db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute('''CREATE TABLE IF NOT EXISTS products
#                               (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
#
#     def save(self):
#         with ConnectDb(self.db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute('INSERT INTO products (id, name, price) VALUES (?, ?, ?)',
#                            (self.id, self.name, self.price))
#
#     @classmethod
#     def fetch_all(cls):
#         with ConnectDb(cls.db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute('SELECT * FROM products')
#             return cursor.fetchall()
#
#     @classmethod
#     def delete_by_id(cls, product_id):
#         with ConnectDb(cls.db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

""""""
import os

import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
db_params = {
    'database': os.getenv('DATABASE'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
}


class ConnectDB:
    def __init__(self):
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = psycopg2.connect(**db_params)
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()


class Product:
    def __init__(self, id, product_name, price):
        self.id = id
        self.product_name = product_name
        self.price = price

    @staticmethod
    def create_table():
        with ConnectDB() as db:
            db.cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY, 
                    product_name VARCHAR(255), 
                    price FLOAT
                )
            """)

    def save(self):
        with ConnectDB() as db:
            insert_into_products = """
                INSERT INTO products (id, product_name, price)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """
            db.cur.execute(insert_into_products, (self.id, self.product_name, self.price))
            print('Successfully saved')

    @classmethod
    def fetch_all(cls):
        with ConnectDB() as db:
            db.cur.execute("SELECT * FROM products")
            return db.cur.fetchall()


# Example usage
# Create the products table
Product.create_table()

# Add a new product
samsung = Product(1, 'Samsung', 1200.00)
samsung.save()

# Fetch all products
products = Product.fetch_all()
print(products)
