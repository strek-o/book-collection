from ..database.db import connect


def read_authors():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Authors"
    cursor.execute(query)
    authors = cursor.fetchall()
    conn.close()
    return authors


def read_books():
    conn = connect()
    cursor = conn.cursor()
    query = '''
        SELECT 
            Books.book_id, Books.title, Authors.name AS author_name, 
            Authors.surname AS author_surname, Genres.name AS genre_name, 
            Books.release_year
        FROM Books
        INNER JOIN Authors ON Books.author_id = Authors.author_id
        INNER JOIN Genres ON Books.genre_id = Genres.genre_id
    '''
    cursor.execute(query)
    books = cursor.fetchall()
    conn.close()
    return books


def read_genres():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Genres"
    cursor.execute(query)
    genres = cursor.fetchall()
    conn.close()
    return genres


def search_authors(author_id=None, name=None, surname=None, nationality=None):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Authors WHERE 1=1"
    params = []

    if author_id:
        query += " AND author_id = ?"
        params.append(author_id)
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


def search_books(book_id=None, title=None, author_id=None, genre_id=None,
                 release_year=None):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Books WHERE 1=1"
    params = []

    if book_id:
        query += " AND book_id = ?"
        params.append(book_id)
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


def search_genres(genre_id=None, name=None):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Genres WHERE 1=1"
    params = []

    if genre_id:
        query += " AND genre_id = ?"
        params.append(genre_id)
    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")

    cursor.execute(query, params)
    genres = cursor.fetchall()
    conn.close()
    return genres
