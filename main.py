import user
import book
import author



def user_validation():
    while not user.current_signed_in_user:
        acc_query = input('''
    Do you have an account with us? Yes/No: ''').lower()
        if acc_query == 'yes':
            try:
                user.sign_in()
            except Exception as e:
                print(e)
        elif acc_query == 'no':
            try:
                user.sign_up()
            except Exception as e:
                print(e)
        else:
            print('Please enter a valid input!')
def main():
    if not user.current_signed_in_user:
        user_validation()
        if user.current_signed_in_user:
            while True:
                menu = input(f"""
                            
Welcome to Blakes Library!
    
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Exit

What would you like to do?: """)
                if menu == '1':
                    book_operations()
                elif menu == '2':
                    user_operations()
                elif menu == '3':
                    author_operations()

def book_operations():
    while True:
        book_op = input('''
Welcome to book operations!

    1. Add a book to the library
    2. Borrow a book from the library
    4. Return a book
    5. Search for a book
    6. Display all books
    7. Return to the main menu
    
What would you like to do?: ''')
        if book_op == '1':
            book.add_book()
        elif book_op == '2':
            book.borrow_book()
        elif book_op == '3':
            book.return_book()
        elif book_op == '4':
            book.return_book()
        elif book_op == '5':
            book.search(book.library)
        elif book_op == '6':
            book.display_books(book.library)
        elif book_op == '7':
            return
        else:
            print('Please enter a valid input')

def user_operations():
    while True:
        user_choice = input(f'''
Welcome to book operations {user.current_signed_in_user.get_username()}!

    1. Logout
    2. View all users
    3. View Account details
    4. Return to menu
    
What would you like to do?: ''')
        if user_choice == '1':
            user.sign_out()
            user_validation()
        elif user_choice == '2':
            user.display_users()
        elif user_choice == '3':
            user.view_account_details()
        elif user_choice == '4':
            return
        else:
            print('Please enter a valid input!')


def author_operations():
    while True:
        author_choice = input(f'''
    Welcome to Author operations {user.current_signed_in_user.get_username()}!

        1. Add a new author
        2. Search for an Author
        3. Display all authors
        4. Return to menu

    What would you like to do?: ''')
        if author_choice == '1':
            author.add_author()
        elif author_choice == '2':
            author.search_author()
        elif author_choice == '3':
            author.view_authors(author.authors)
        elif author_choice == '4':
            return
        else:
            print('Please enter a valid input!')
            
main()