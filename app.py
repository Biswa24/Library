import utils
Selection = """
You want to use Text-File Based or SQL Based Database, Enter
'T' for Text-File Based Database
'S' for SQL Based Database
"""
while(True):
    type = input(Selection)
    if type == 'T' or type == 't':
        from utils import Text_File_Database
        database = Text_File_Database
        break
    elif type == 'S' or type == 's':
        from utils import Sql_Database
        database = Sql_Database
        break
    else:
        print("\nTry again....")


USER_CHOICE = """
Enter:
'a' to add a new book
'l' to list all books
'r' to mark a book as read
'd' to delete a book
'q' to quit
Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("\n Try again...")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.add_book(name, author)


def list_books():
    k = database.get_all_books()
    if (k==[]):
        print("\nNo books are in library to display.")
    for book in k:
        read = 'YES' if book[2] else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f'{book[0]} by {book[1]} — Read: {read}')


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    author = input('Enter the new book author: ')

    database.mark_book_as_read(name,author)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    author = input('Enter the new book author: ')

    database.delete_book(name, author)


menu()
