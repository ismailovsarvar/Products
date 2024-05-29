import os

import psycopg2
from dotenv import load_dotenv

# .env fayldagi o'zgaruvchilarni yuklash
load_dotenv()
db_params = {
    'database': os.getenv('database'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port'),
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
                    id INT PRIMARY KEY, 
                    product_name VARCHAR (255), 
                    price FLOAT
                )
            """)

    def save(self):
        with ConnectDB() as db:
            insert_into_products = """
                INSERT INTO products (id, product_name, price)
                VALUES (%s,%s,%s)
                ON CONFLICT (id) DO NOTHING;
            """
            db.cur.execute(insert_into_products, (self.id, self.product_name, self.price))
            print('Successfully saved')

    @classmethod
    def fetch_all(cls):
        with ConnectDB() as db:
            db.cur.execute("""SELECT * FROM products;""")
            return db.cur.fetchall()


# Product table yaratish
Product.create_table()

# Yangi product qo'shish
# samsung = Product(1, 'Samsung', '1200.00')
# samsung.save()
samsung1 = Product(2, 'Samsung S24 Ultra', '1500.00')
samsung1.save()

# Barcha productlarni chop etish
products = Product.fetch_all()
print(products)
