import book_collection.schemas as schemas
import book_collection.models as m
import book_collection.service as s
import pandas as pd


def main():
    schemas.Authors.create_table()
    schemas.Genres.create_table()
    schemas.Books.create_table()

    author = m.Author("J.R.R.", "Tolkien", 1892, "British")
    genre = m.Genre("Fantasy")
    book = m.Book("The Hobbit", 1, 1, 1937)
    s.create_author(author.name, author.surname, author.birth_date, author.national)
    s.create_genre(genre.name)
    s.create_book(book.title, 1, 1, book.release_year)

    a = pd.DataFrame(s.read_authors())
    g = pd.DataFrame(s.read_genres())
    b = pd.DataFrame(s.read_books())
    print(a)
    print(g)
    print(b)

    # print(s.read_authors()) 
    # print(s.read_genres())
    # print(s.read_books())

    schemas.Authors.drop_table()
    schemas.Books.drop_table()
    schemas.Genres.drop_table()


if __name__ == '__main__':
    main()
