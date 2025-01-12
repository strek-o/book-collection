from ..interface.create_menu import create_menu
from ..interface.read_menu import read_menu
from ..interface.update_menu import update_menu
from ..interface.delete_menu import delete_menu
from ..utils import clear


def main_menu():
    clear()
    while True:
        print("\n\t\t=== Book Collection ===")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        action = input("Choose an option <1-5>: ")

        if action == '1':
            create_menu()

        elif action == '2':
            read_menu()

        elif action == '3':
            update_menu()

        elif action == '4':
            delete_menu()

        elif action == '5':
            print("\n\tExiting the program. Goodbye!\n")
            break

        else:
            print("\nError:\tInvalid option.\n"
                  "\tPlease try again.\n")
