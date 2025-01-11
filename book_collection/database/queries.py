from .db import connect


def create_author(name, surname, birth_date, nationality):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Authors (name, surname, birth_date, nationality)
        VALUES (?, ?, ?, ?)
    ''', (name, surname, birth_date, nationality))
    conn.commit()
    conn.close()


def read_authors():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Authors
    ''')
    authors = cursor.fetchall()
    conn.close()
    return authors


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


def create_genre(genre):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Genres (genre)
        VALUES (?)
    ''', (genre,))
    conn.commit()
    conn.close()


def read_genres():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Genres
    ''')
    genres = cursor.fetchall()
    conn.close()
    return genres
