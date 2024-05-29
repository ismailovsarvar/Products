import psycopg2
from colorama import Fore, Style

# PostgreSQL server ma'lumotlariga ulanish
db_name = 'postgres'
password = '5'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(dbname=db_name,
                        user=user,
                        password=password,
                        host=host,
                        port=port)
cur = conn.cursor()


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # @staticmethod
    # def create_users_table():
    #     try:
    #         create_table_query = '''CREATE TABLE users (
    #             id SERIAL PRIMARY KEY,
    #             username VARCHAR(255) UNIQUE NOT NULL,
    #             email VARCHAR(255) UNIQUE NOT NULL
    #         )'''
    #         cur.execute(create_table_query)
    #         conn.commit()
    #         print(f"{Fore.GREEN}Users table created successfully!{Style.RESET_ALL}")
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(f"{Fore.RED}Error creating users table: {error}{Style.RESET_ALL}")
    #         if error.pgcode == '42P07':
    #             print(f"{Fore.YELLOW}Users table already exists. Skipping creation.{Style.RESET_ALL}")
    #
    # create_users_table()

    # def save(self):
    #     try:
    #         insert_query = '''INSERT INTO users (username, email) VALUES (%s, %s)'''
    #         cur.execute(insert_query, (self.username, self.email))
    #         conn.commit()
    #
    #         print(f"{Fore.GREEN}User saved successfully{Style.RESET_ALL}")
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(f"{Fore.RED}Error saving user: {error}{Style.RESET_ALL}")

    @staticmethod
    def get_all():
        try:
            select = '''SELECT * FROM users'''
            cur.execute(select)
            rows = cur.fetchall()
            users = []
            for row in rows:
                us = User(row[1], row[2])
                users.append(us)
            return users
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"{Fore.RED}Error fetching user: {error}{Style.RESET_ALL}")
            return []


# ADD USERS
# user_1 = User("Sarvar", "sarvar@gmail.com")
# user_2 = User("Siroj", "siroj@gmail.com")
# user_3 = User("Muslima", "muslima@gmail.com")
# user_1.save()
# user_2.save()
# user_3.save()

all_users = User.get_all()
print(f"{Fore.MAGENTA}List of all users:{Style.RESET_ALL}")
for user in all_users:
    print(f"{Fore.YELLOW}Username:{Style.RESET_ALL} {user.username}, {Fore.YELLOW}Email:{Style.RESET_ALL} {user.email}")
