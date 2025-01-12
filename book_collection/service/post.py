from ..database.db import connect


def create_author(name, surname, birth_date, nationality):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(''' 
        INSERT INTO Authors (name, surname, birth_date, nationality)
        VALUES (?, ?, ?, ?)
    ''', (name, surname, birth_date, nationality))
    conn.commit()
    conn.close()
    return True


def create_book(title, author_id, genre_id, release_year):
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
        SELECT COUNT(*) FROM Genres WHERE genre_id = ?
    ''', (genre_id,))
    if cursor.fetchone()[0] == 0:
        conn.close()
        print(f"\nError:\tGenre with ID {genre_id} does not exist.\n"
              "\tPlease enter a valid genre ID.\n")
        return False

    cursor.execute(''' 
        INSERT INTO Books (title, author_id, genre_id, release_year)
        VALUES (?, ?, ?, ?)
    ''', (title, author_id, genre_id, release_year))
    conn.commit()
    conn.close()
    return True


def create_genre(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(''' 
        INSERT INTO Genres (name)
        VALUES (?)
    ''', (name,))
    conn.commit()
    conn.close()
    return True
