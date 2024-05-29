from collections import namedtuple

# Define the namedtuples
Product = namedtuple('Product', ['id', 'name', 'price', 'quantity'])
Person = namedtuple('Person', ['first_name', 'last_name', 'age', 'email'])

# Create instances of Product
product1 = Product(id=1, name='Laptop', price=1200.00, quantity=5)
product2 = Product(id=2, name='Smartphone', price=800.00, quantity=10)

# Create instances of Person
person1 = Person(first_name='John', last_name='Doe', age=30, email='john.doe@example.com')
person2 = Person(first_name='Jane', last_name='Smith', age=25, email='jane.smith@example.com')

# Accessing fields and printing
print(f"Product 1: {product1.name} costs ${product1.price} and we have {product1.quantity} in stock.")
print(f"Product 2: {product2.name} costs ${product2.price} and we have {product2.quantity} in stock.")
print(f"Person 1: {person1.first_name} {person1.last_name} is {person1.age} years old and can be contacted at {person1.email}.")
print(f"Person 2: {person2.first_name} {person2.last_name} is {person2.age} years old and can be contacted at {person2.email}.")
