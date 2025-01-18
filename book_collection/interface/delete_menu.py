from ..service import *


def delete_menu():
    while True:
        print("\n\t\t--- Delete Menu ---")
        print("1. Delete Author")
        print("2. Delete Book")
        print("3. Delete Genre")
        print("4. Go Back")
        action = input("Choose an option <1-4>: ")

        if action == '1':
            author_id = int(input("Enter author ID: "))
            res = delete_author(author_id)
            if res:
                print("\nOK:\tAuthor deleted successfully.\n")
            break

        elif action == '2':
            book_id = int(input("Enter book ID: "))
            res = delete_book(book_id)
            if res:
                print("\nOK:\tBook deleted successfully.\n")
            break

        elif action == '3':
            genre_id = int(input("Enter genre ID: "))
            res = delete_genre(genre_id)
            if res:
                print("\nOK:\tGenre deleted successfully.\n")
            break

        elif action == '4':
            break

        else:
            print("\nError:\tInvalid option.\n"
                  "\tPlease try again.\n")
