# By Ismailov Sarvar N47 group
"""
1 - assignment
"""

import psycopg2
import requests

url = f'https://dummyjson.com/users'
r = requests.get(url)
# print(r.status_code, r.text)

# PostgreSQL server ma'lumotlariga ulanish
db_name = 'postgres'
host = 'localhost'
port = 5432
user = 'postgres'
password = '5'
try:
    conn = psycopg2.connect(dbname=db_name,
                            host=host,
                            port=port,
                            user=user,
                            password=password)

    cur = conn.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        firstName varchar(150) NOT NULL, lastName varchar(150) NOT NULL,
        maidenName varchar(150) NOT NULL, age INT NOT NULL,
        gender varchar(150) NOT NULL, email varchar(150) NOT NULL,
        phone varchar(150) NOT NULL, username varchar(150) NOT NULL,
        password varchar(150) NOT NULL, birthDate varchar(150) NOT NULL,
        image varchar(150) NOT NULL, height INT NOT NULL, weight FLOAT NOT NULL,
        university varchar(150) NOT NULL)'''

    # cur.execute(create_table_query)
    # conn.commit()
    # print("Table created successfully")

    insert_into_query = '''INSERT INTO users (firstName, lastName, maidenName, 
        age, gender, email, phone, username, password, birthDate, image, 
        height, weight, university) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    # users = r.json()['users']
    #
    # for user in users:
    #     cur.execute(insert_into_query, (user['firstName'],
    #                                     user['lastName'], user['maidenName'], user['age'],
    #                                     user['gender'], user['email'],
    #                                     user['phone'], user['username'],
    #                                     user['password'], user['birthDate'],
    #                                     user['image'], user['height'],
    #                                     user['weight'], user['university']))
    #     conn.commit()
    print("Data inserted successfully")
except psycopg2.Error as e:
    print(e)
finally:
    cur.close()
    conn.close()

"""
2 - assignment
"""
from collections import namedtuple
from colorama import Fore, Style

# namedtuple
Product = namedtuple('Product', ['id', 'name', 'price', 'quantity'])
Person = namedtuple('Person', ['firstName', 'lastName', 'age', 'gender', 'email'])

# Creating a product
product1 = Product(id=1, name='Laptop', price=1200.50, quantity=5)
product2 = Product(id=2, name='Smartphone', price=800.20, quantity=10)

# Creating a person
person1 = Person(firstName='Sarvar', lastName='Ismailov',
                 age=29, gender='Male', email='sarvar@gmail.com')
person2 = Person(firstName='Sardor', lastName='Gafurov',
                 age=25, gender='Male', email='sardor@gmail.com')

# Printing
print(f"{Fore.GREEN}Product 1{Style.RESET_ALL}: {Fore.CYAN}{product1.name}{Style.RESET_ALL} costs ${Fore.CYAN}{product1.price}{Style.RESET_ALL} and we have {Fore.CYAN}{product1.quantity}{Style.RESET_ALL} in stock.")
print(f"{Fore.GREEN}Product 2{Style.RESET_ALL}: {Fore.CYAN}{product2.name}{Style.RESET_ALL} costs ${Fore.CYAN}{product2.price}{Style.RESET_ALL} and we have {Fore.CYAN}{product2.quantity}{Style.RESET_ALL} in stock.")
print(
    f"{Fore.GREEN}Person 1{Style.RESET_ALL}: {Fore.LIGHTYELLOW_EX}{person1.firstName} {person1.lastName}{Style.RESET_ALL} is {person1.age} years old and can be contacted at {person1.email}.")
print(
    f"{Fore.GREEN}Person 2{Style.RESET_ALL}: {Fore.LIGHTYELLOW_EX}{person2.firstName} {person2.lastName}{Style.RESET_ALL} is {person2.age} years old and can be contacted at {person2.email}.")
