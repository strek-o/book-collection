from ..database.db import connect


def delete_author(author_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM Authors WHERE author_id = ?
    ''', (author_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        raise ValueError(f"\n\nAuthor with ID {author_id} does not exist.\n")

    cursor.execute('''
        SELECT COUNT(*) FROM Books WHERE author_id = ?
    ''', (author_id,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        raise ValueError(f"\n\nAuthor with ID {author_id} is assigned to at least one book and cannot be deleted.\n")

    cursor.execute('''
        DELETE FROM Authors WHERE author_id = ?
    ''', (author_id,))
    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM Books WHERE book_id = ?
    ''', (book_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        raise ValueError(f"\n\nBook with ID {book_id} does not exist.\n")

    cursor.execute('''
        DELETE FROM Books WHERE book_id = ?
    ''', (book_id,))
    conn.commit()
    conn.close()


def delete_genre(genre_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM Genres WHERE genre_id = ?
    ''', (genre_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        raise ValueError(f"\n\nGenre with ID {genre_id} does not exist.\n")

    cursor.execute('''
        SELECT COUNT(*) FROM Books WHERE genre_id = ?
    ''', (genre_id,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        raise ValueError(f"\n\nGenre with ID {genre_id} is assigned to at least one book and cannot be deleted.\n")

    cursor.execute('''
        DELETE FROM Genres WHERE genre_id = ?
    ''', (genre_id,))
    conn.commit()
    conn.close()
