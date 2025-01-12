import book_collection.schemas as schemas
from book_collection.interface.main_menu import main_menu


def main():
    schemas.Authors.create_table()
    schemas.Genres.create_table()
    schemas.Books.create_table()

    main_menu()

    # schemas.Authors.drop_table()
    # schemas.Books.drop_table()
    # schemas.Genres.drop_table()


if __name__ == '__main__':
    main()
