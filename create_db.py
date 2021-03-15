from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

DB_USER = "postgres"
DB_HOST = "localhost"
DB_PASSWORD = "coderslab"

CREATE_DB = "CREATE DATABASE workshop;"

CREATE_USERS_TABLE = """CREATE TABLE users(
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(255) UNIQUE,
                    hashed_password VARCHAR(80)
                    );"""

CREATE_MESSAGES_TABLE = """CREATE TABLE messages(
                            id SERIAL PRIMARY KEY,
                            from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                            to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                            text VARCHAR(255),
                            creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            );"""

try:
    cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase:
        print("Database already exist")
    cnx.close()
except OperationalError:
    print("Database creating error!")


try:
    cnx = connect(database="workshop", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_USERS_TABLE)
        print("User table created")
    except DuplicateTable:
        print("User table already exist")
    cnx.close()
except OperationalError:
    print("Table creating error!")


try:
    cnx = connect(database="workshop", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print("Messages table created")
    except DuplicateTable:
        print("Messages table already exist")
    cnx.close()
except OperationalError:
    print("Table creating error!")