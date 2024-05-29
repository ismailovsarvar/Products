from datetime import datetime

import psycopg2

# PostgreSQL server ma'lumotlari
db_name = 'postgres'
password = '5'
host = 'localhost'
port = 5432
user = 'postgres'

with psycopg2.connect(dbname=db_name,
                      user=user,
                      password=password,
                      host=host,
                      port=port) as conn:
    with conn.cursor() as cur:
        # Funksiyalarni yaratamiz:
        def create_table():
            cur.execute('''CREATE TABLE IF NOT EXISTS Products (
                            id SERIAL PRIMARY KEY,
                            name TEXT NOT NULL,
                            image TEXT,
                            is_liked BOOLEAN,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            );''')
            conn.commit()
            # conn.close()


        def insert_products_data(name, image, is_liked):
            cur.execute('''INSERT INTO Products (name, image, is_liked) VALUES (%s, %s, %s)''',
                        (name, image, is_liked))
            conn.commit()
            # conn.close()


        def select_data():
            cur.execute('''SELECT * FROM Products''')
            rows = cur.fetchall()
            # conn.close()
            return rows


        def update_data(product_id, name=None, image=None, is_liked=None):
            query = '''UPDATE Products SET updated_at = %s'''
            params = (datetime.now(),)

            if name is not None:
                query += ''', name = %s'''
                params += (name,)
            if image is not None:
                query += ''', image = %s'''
                params += (image,)
            if is_liked is not None:
                query += ''', is_liked = %s'''
                params += (is_liked,)

            query += ''' WHERE id = %s'''
            params += (product_id,)

            cur.execute(query, params)
            conn.commit()
            # conn.close()


        def delete_data(product_id):
            cur.execute('''DELETE FROM Products WHERE id = %s''', (product_id,))
            conn.commit()
            # conn.close()

# Funksiyalarni ishga tushurish
if __name__ == "__main__":
    create_table()

    # Test ma'lumotlarni qo'shish
    insert_products_data("Televizor", "image1.jpg", True)
    insert_products_data("Changyutgich", "image2.jpg", False)
    insert_products_data("Kirmashina", "image2.jpg", False)

    # Test ma'lumotlarni tanlash
    print("All Products:")
    print(select_data())

    # Test ma'lumotni yangilash
    update_data(1, name="Updated Product 1", is_liked=False)
    print("After Update:")
    print(select_data())

    # Test ma'lumotni o'chirish
    delete_data(2)
    print("After Delete:")
    print(select_data())
