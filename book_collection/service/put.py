from ..database.db import connect


def update_author(author_id, name=None, surname=None, birth_date=None, nationality=None):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE Authors SET"
    updates = []
    params = []

    cursor.execute("SELECT COUNT(*) FROM Authors WHERE author_id = ?", (author_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        raise ValueError(f"\n\nAuthor with ID {author_id} does not exist.\n")

    if name:
        updates.append("name = ?")
        params.append(name)
    if surname:
        updates.append("surname = ?")
        params.append(surname)
    if birth_date:
        updates.append("birth_date = ?")
        params.append(birth_date)
    if nationality:
        updates.append("nationality = ?")
        params.append(nationality)

    if updates:
        query += " " + ", ".join(updates) + " WHERE author_id = ?"
        params.append(author_id)
        cursor.execute(query, params)

    conn.commit()
    conn.close()


def update_book(book_id, title=None, author_id=None, genre_id=None, release_year=None):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE Books SET"
    updates = []
    params = []

    cursor.execute("SELECT COUNT(*) FROM Books WHERE book_id = ?", (book_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        raise ValueError(f"\n\nBook with ID {book_id} does not exist.\n")

    if author_id:
        cursor.execute("SELECT COUNT(*) FROM Authors WHERE author_id = ?", (author_id,))
        if cursor.fetchone()[0] == 0:
            conn.close()
            raise ValueError(f"\n\nAuthor with id {author_id} does not exist.\n")

    if genre_id:
        cursor.execute("SELECT COUNT(*) FROM Genres WHERE genre_id = ?", (genre_id,))
        if cursor.fetchone()[0] == 0:
            conn.close()
            raise ValueError(f"\n\nGenre with ID {genre_id} does not exist.\n")

    if title:
        updates.append("title = ?")
        params.append(title)
    if author_id:
        updates.append("author_id = ?")
        params.append(author_id)
    if genre_id:
        updates.append("genre_id = ?")
        params.append(genre_id)
    if release_year:
        updates.append("release_year = ?")
        params.append(release_year)

    if updates:
        query += " " + ", ".join(updates) + " WHERE book_id = ?"
        params.append(book_id)
        cursor.execute(query, params)

    conn.commit()
    conn.close()


def update_genre(genre_id, name=None):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE Genres SET"
    updates = []
    params = []

    cursor.execute("SELECT COUNT(*) FROM Genres WHERE genre_id = ?", (genre_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        raise ValueError(f"\n\nGenre with ID {genre_id} does not exist.\n")

    if name:
        updates.append("name = ?")
        params.append(name)

    if updates:
        query += " " + ", ".join(updates) + " WHERE genre_id = ?"
        params.append(genre_id)
        cursor.execute(query, params)

    conn.commit()
    conn.close()
