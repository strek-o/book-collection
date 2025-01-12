from ..database.db import connect


def read_authors(name=None, surname=None, nationality=None):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Authors WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if surname:
        query += " AND surname LIKE ?"
        params.append(f"%{surname}%")
    if nationality:
        query += " AND nationality LIKE ?"
        params.append(f"%{nationality}%")

    cursor.execute(query, params)
    authors = cursor.fetchall()
    conn.close()
    return authors


def read_books(title=None, author_id=None, genre_id=None, release_year=None):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Books WHERE 1=1"
    params = []

    if title:
        query += " AND title LIKE ?"
        params.append(f"%{title}%")
    if author_id:
        query += " AND author_id = ?"
        params.append(author_id)
    if genre_id:
        query += " AND genre_id = ?"
        params.append(genre_id)
    if release_year:
        query += " AND release_year LIKE ?"
        params.append(f"%{release_year}%")

    cursor.execute(query, params)
    books = cursor.fetchall()
    conn.close()
    return books


def read_genres(name=None):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Genres WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")

    cursor.execute(query, params)
    genres = cursor.fetchall()
    conn.close()
    return genres
