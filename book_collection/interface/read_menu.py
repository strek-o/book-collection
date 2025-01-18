from ..service import *
import pandas as pd


def read_menu():
    while True:
        print("\n\t\t--- Read Menu ---")
        print("1. View Authors")
        print("2. View Books")
        print("3. View Genres")
        print("4. Go Back")
        action = input("Choose an option <1-4>: ")

        if action == '1':
            data = pd.DataFrame(
                read_authors(),
                columns=["ID", "name", "surname", "birth date", "nationality"]
            )
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(data)
            break

        elif action == '2':
            data = pd.DataFrame(
                read_books(),
                columns=["ID", "title", "author_name", "author_surname",
                         "genre", "release year"]
            )
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(data)
            break

        elif action == '3':
            data = pd.DataFrame(
                read_genres(),
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
