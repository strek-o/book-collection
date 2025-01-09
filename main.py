from components import *


def main():
    initialize_database()

    author = mA.Author("J.R.R.", "Tolkien", 1892, "British")
    genre = mG.Genre("Fantasy")
    book = mB.Book("The Hobbit", 1, 1, 1937)
    q.create_author(author.name, author.surname, author.birth_date, author.nationality)
    q.create_genre(genre.name)
    q.create_book(book.title, book.author_id, book.genre_id, book.release_year)
    print(q.read_authors())
    print(q.read_genres())
    print(q.read_books())

    terminate_database()


if __name__ == '__main__':
    main()
