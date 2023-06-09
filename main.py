from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

CREATE_DB = 'CREATE DATABASE workshop'

CREATE_USERS = 'CREATE TABLE users (id serial PRIMARY KEY, username varchar(255) UNIQUE, hashed_password varchar(80))'

CREATE_MESSAGES = """CREATE TABLE messages(
    id SERIAL, 
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

DB_USER = "postgres"
DB_HOST = "127.0.0.1"
DB_PASSWORD = "coderslab"


try:
    cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as error:
        print(f'Database already exists\n {error}')
    cnx.close()
except OperationalError as error:
    print(f'Connection error\n {error}')

try:
    cnx = connect(database="workshop", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()

    try:
        cursor.execute(CREATE_USERS)
        print("Table users created")
    except DuplicateTable as error:
        print(f'Table already exists\n {error}')

    try:
        cursor.execute(CREATE_MESSAGES)
        print("Table messages created")
    except DuplicateTable as error:
        print(f'Table already exists\n {error}')
    cnx.close()
except OperationalError as error:
    print("Connection Error: ", error)
