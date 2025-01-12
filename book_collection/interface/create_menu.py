from ..models import *
from ..service import *
from ..utils import get_date, validate_date, get_year, get_author, get_genre


def create_menu():
    while True:
        print("\n\t\t--- Create Menu ---")
        print("1. Add Author")
        print("2. Add Book")
        print("3. Add Genre")
        print("4. Go Back")
        action = input("Choose an option <1-4>: ")

        if action == '1':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            birth_date = get_date()
            birth_date = validate_date(birth_date)
            nationality = input("Enter nationality: ")

            a = Author(name, surname, birth_date, nationality)
            no_err = create_author(a.name, a.surname, a.birth_date, a.nationality)
            if no_err:
                print("\nOK:\tAuthor created successfully.\n")
            break

        elif action == '2':
            title = input("Enter title: ")
            author_id = get_author()
            genre_id = get_genre()
            release_year = get_year()

            b = Book(title, author_id, genre_id, release_year)
            no_err = create_book(b.title, b.author_id, b.genre_id, b.release_year)
            if no_err:
                print("\nOK:\tBook created successfully.\n")
            break

        elif action == '3':
            name = input("Enter name: ")
            g = Genre(name)
            no_err = create_genre(g.name)
            if no_err:
                print("\nOK:\tGenre created successfully.\n")
            break

        elif action == '4':
            break

        else:
            print("\nError:\tInvalid option.\n"
                  "\tPlease try again.\n")
