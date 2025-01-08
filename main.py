from schemas.Books import create_table, drop_table
from service import queries as q
from models.Book import *


def main():
    create_table()
    book = Book("The Hobbit", 1, 1, 1937)
    q.create_book(book.title, book.author_id, book.genre_id, book.release_year)
    print(q.read_books())
    drop_table()


if __name__ == '__main__':
    main()
