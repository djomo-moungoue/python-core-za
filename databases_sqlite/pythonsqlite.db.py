import sqlite3
from sqlite3 import Error

def create_connection_ROM(db_file):
    """
    create a database connection to a SQLite database
    """
    conn_ROM = None
    try:
        conn_ROM = sqlite3.connect(db_file)
        print('ROM : '+sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn_ROM:
            conn_ROM.close()

def create_connection_RAM():
    """
    create a database connection to a SQLite database
    """
    conn_RAM = None
    try:
        conn_RAM = sqlite3.connect(':memory:')
        print('RAM : '+sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn_RAM:
            conn_RAM.close()

if __name__ == '__main__':
    create_connection_ROM(r"/PythonCore/databases_sqlite/pythonsqlite.db.py")
    create_connection_RAM()
