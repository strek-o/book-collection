import re
from datetime import datetime
from ..service import read_authors, read_genres, read_books
import os


def get_date():
    while True:
        birth_date = input("Enter birth date <DD/MM/YYYY>: ")
        if re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", birth_date):
            break
        else:
            print("\nError:\tInvalid date.\n"
                  "\tPlease enter a valid date.\n")
    return birth_date


def validate_date(birth_date):
    while True:
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            current_year = datetime.today().year
            if 1000 <= int(birth_date[-4:]) <= current_year:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nError:\tInvalid date.\n"
                  "\tPlease enter a valid date.\n")
            birth_date = input("Enter birth date <DD/MM/YYYY>: ")
    return birth_date


def get_year():
    while True:
        try:
            release_year = int(input("Enter release year <YYYY>: "))
            current_year = datetime.today().year
            if 1000 <= release_year <= current_year:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nError:\tInvalid release year.\n"
                  "\tPlease enter a valid year.\n")
    return release_year


def get_author():
    while True:
        try:
            author_id = int(input("Enter author ID: "))
            if len(read_authors(author_id)) > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nError:\tInvalid author ID.\n"
                  "\tPlease enter a valid ID.\n")
    return author_id


def get_book():
    while True:
        try:
            book_id = int(input("Enter book ID: "))
            if len(read_books(book_id)) > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nError:\tInvalid book ID.\n"
                  "\tPlease enter a valid ID.\n")
    return book_id


def get_genre():
    while True:
        try:
            genre_id = int(input("Enter genre ID: "))
            if len(read_genres(genre_id)) > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nError:\tInvalid genre ID.\n"
                  "\tPlease enter a valid ID.\n")
    return genre_id


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_name():
    while True:
        name = input("Enter name: ")
        if name:
            break
        else:
            print("\nError:\tName cannot be empty.\n"
                  "\tPlease enter a valid name.\n")
    return name


def get_surname():
    while True:
        surname = input("Enter surname: ")
        if surname:
            break
        else:
            print("\nError:\tSurname cannot be empty.\n"
                  "\tPlease enter a valid surname.\n")
    return surname


def get_nationality():
    while True:
        nationality = input("Enter nationality: ")
        if nationality:
            break
        else:
            print("\nError:\tNationality cannot be empty.\n"
                  "\tPlease enter a valid nationality.\n")
    return nationality


def get_title():
    while True:
        title = input("Enter title: ")
        if title:
            break
        else:
            print("\nError:\tTitle cannot be empty.\n"
                  "\tPlease enter a valid title.\n")
    return title
