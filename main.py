from book_collection.database import queries as q
from book_collection.schemas import Authors as sA
from book_collection.schemas import Books as sB
from book_collection.schemas import Genres as sG
from book_collection.models import Author as mA
from book_collection.models import Book as mB
from book_collection.models import Genre as mG


def main():
    sA.create_table()
    sG.create_table()
    sB.create_table()

    author = mA.Author("J.R.R.", "Tolkien", 1892, "British")
    genre = mG.Genre("Fantasy")
    book = mB.Book("The Hobbit", 1, 1, 1937)
    q.create_author(author.name, author.surname, author.birth_date, author.nationality)
    q.create_author(author.name, author.surname, author.birth_date, author.nationality)
    q.create_genre(genre.name)
    q.create_book(book.title, book.author_id, book.genre_id, book.release_year)
    print(q.read_authors())
    print(q.read_genres())
    print(q.read_books())

    sA.drop_table()
    sG.drop_table()
    sB.drop_table()


if __name__ == '__main__':
    main()
