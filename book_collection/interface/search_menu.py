from ..service import *
import pandas as pd


def search_menu():
    while True:
        print("\n\t\t--- Search Menu ---")
        print("1. View Authors")
        print("2. View Books")
        print("3. View Genres")
        print("4. Go Back")
        action = input("Choose an option <1-4>: ")

        if action == '1':
            print("[press Enter to skip]")
            id_filter = input("Filter by ID: ")
            name_filter = input("Filter by name: ")
            surname_filter = input("Filter by surname: ")
            nationality_filter = input("Filter by nationality: ")
            data = pd.DataFrame(
                search_authors(id_filter, name_filter, surname_filter,
                               nationality_filter),
                columns=["ID", "name", "surname", "birth date", "nationality"]
            )
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(data)
            break

        elif action == '2':
            print("[press Enter to skip]")
            id_filter = input("Filter by ID: ")
            title_filter = input("Filter by title: ")
            author_id_filter = input("Filter by author ID: ")
            genre_id_filter = input("Filter by genre ID: ")
            release_year_filter = input("Filter by release year: ")
            data = pd.DataFrame(
                search_books(id_filter, title_filter, author_id_filter,
                             genre_id_filter, release_year_filter),
                columns=["ID", "title", "author ID", "genre ID",
                         "release year"]
            )
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(data)
            break

        elif action == '3':
            print("[press Enter to skip]")
            id_filter = input("Filter by ID: ")
            name_filter = input("Filter by name: ")
            data = pd.DataFrame(
                search_genres(id_filter, name_filter),
                columns=["ID", "name"]
            )
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(data)
            break

        elif action == '4':
            break

        else:
            print("\nError:\tInvalid option.\n"
                  "\tPlease try again.\n")
