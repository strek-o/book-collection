from config.database import *


def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title TEXT NOT NULL,
            author_id INTEGER,
            genre_id INTEGER NOT NULL,
            release_year INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def drop_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Books
    ''')
    conn.commit()
    conn.close()
