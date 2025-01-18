from ..models import *
from ..service import *
from ..utils import *


def update_menu():
    while True:
        print("\n\t\t--- Update Menu ---")
        print("1. Update Author")
        print("2. Update Book")
        print("3. Update Genre")
        print("4. Go Back")
        action = input("Choose an option <1-4>: ")

        if action == '1':
            author_id = get_author()
            name = get_name()
            surname = get_surname()
            birth_date = get_date()
            birth_date = validate_date(birth_date)
            nationality = get_nationality()

            current_author = search_authors(author_id=author_id)[0]
            updated_author = Author(
                name or current_author.name,
                surname or current_author.surname,
                birth_date or current_author.birth_date,
                nationality or current_author.nationality
            )
            no_err = update_author(
                author_id,
                updated_author.name,
                updated_author.surname,
                updated_author.birth_date,
                updated_author.nationality
            )
            if no_err:
                print("\nOK:\tAuthor updated successfully.\n")
            break

        elif action == '2':
            book_id = get_book()
            title = get_title()
            author_id = get_author()
            genre_id = get_genre()
            new_year = get_year()

            current_book = search_books(book_id=book_id)[0]
            updated_book = Book(
                title or current_book.title,
                int(author_id) if author_id else current_book.author_id,
                int(genre_id) if genre_id else current_book.genre_id,
                int(new_year) if new_year else current_book.release_year
            )
            no_err = update_book(
                book_id,
                updated_book.title,
                updated_book.author_id,
                updated_book.genre_id,
                updated_book.release_year
            )
            if no_err:
                print("\nOK:\tBook updated successfully.\n")
            break

        elif action == '3':
            genre_id = get_genre()
            name = get_name()
            current_genre = search_genres(genre_id)[0]
            updated_genre = Genre(name or current_genre.name)
            no_err = update_genre(genre_id, updated_genre.name)
            if no_err:
                print("\nOK:\tGenre updated successfully.\n")
            break

        elif action == '4':
            break

        else:
            print("\nError:\tInvalid option.\n"
                  "\tPlease try again.\n")
