from ..database.db import connect


def delete_author(author_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM Authors WHERE author_id = ?
    ''', (author_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        print(f"\nError:\tAuthor with ID {author_id} does not exist.\n"
              "\tPlease enter a valid author ID.\n")
        return False

    cursor.execute('''
        SELECT COUNT(*) FROM Books WHERE author_id = ?
    ''', (author_id,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        print(f"\nError:\tAuthor with ID {author_id} is assigned to\n"
              "\tat least one book and cannot be deleted.\n")
        return False

    cursor.execute('''
        DELETE FROM Authors WHERE author_id = ?
    ''', (author_id,))
    conn.commit()
    conn.close()
    return True


def delete_book(book_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM Books WHERE book_id = ?
    ''', (book_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        print(f"\nError:\tBook with ID {book_id} does not exist.\n"
              "\tPlease enter a valid book ID.\n")
        return False

    cursor.execute('''
        DELETE FROM Books WHERE book_id = ?
    ''', (book_id,))
    conn.commit()
    conn.close()
    return True


def delete_genre(genre_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM Genres WHERE genre_id = ?
    ''', (genre_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        print(f"\nError:\tGenre with ID {genre_id} does not exist.\n"
              "\tPlease enter a valid genre ID.\n")
        return False

    cursor.execute('''
        SELECT COUNT(*) FROM Books WHERE genre_id = ?
    ''', (genre_id,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        print(f"\nError:\tGenre with ID {genre_id} is assigned to\n"
              "\tat least one book and cannot be deleted.\n")
        return False

    cursor.execute('''
        DELETE FROM Genres WHERE genre_id = ?
    ''', (genre_id,))
    conn.commit()
    conn.close()
    return True
