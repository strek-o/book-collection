from config.database import *


def create_book(title, author_id, genre_id, release_year):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Books (title, author_id, genre_id, release_year)
        VALUES (?, ?, ?, ?)
    ''', (title, author_id, genre_id, release_year))
    conn.commit()
    conn.close()


def read_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Books
    ''')
    books = cursor.fetchall()
    conn.close()
    return books
