from ..database.db import connect


def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genres (
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def drop_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Genres
    ''')
    conn.commit()
    conn.close()
