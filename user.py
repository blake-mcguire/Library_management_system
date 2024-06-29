import re




class User:
    
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__books_on_loan = {}
        
    def get_username(self):
        return self.__name
    
    def set_username(self, new_name):
        self.__name = new_name
    
    def get_password(self):
        return self.__password
    
    def set_password(self, new_pw):
        self.__password = new_pw
    def get_books_loan(self):
        return self.__books_on_loan
    
    def add_book_to_loans(self, book_title, book):
        self.__books_on_loan[book_title] = book
    
    def remove_book_from_loans(self, title):
        if title in self.__books_on_loan:
            del self.__books_on_loan[title]
users = {}
current_signed_in_user = None



def sign_in():
    global current_signed_in_user
    username = input('Enter Your username: ')
    password = input('Enter Your password: ')
    if username in users and users[username].get_password() == password:
        current_signed_in_user = users[username]
        print(f'Welcome back {username}')
    else:
        print('Invalid username or password')
# SIGN UP

def sign_up():
    global current_signed_in_user
    try:
        username = input('What would you like your username to be?: ')
        password = input('What would you like your password to be: ')
        password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#~+=])[A-Za-z\d@$!%*?&#~=+]{8,}$")
        if not password_pattern.match(password):
            print('''
    Password is Weak, Try again.
    Include At least:
    1 UpperCase letter
    1 Special Character
    8 Characters Long...''')
        elif username in users:
            print('That user name is already taken!')
        else:
            new_user = User(username, password)
            users[username] = new_user
            current_signed_in_user = users[username]
            print(f'Welcome {username}!')
    except Exception as e:
        print(e)
        
# takes an inpput of a username and password 
# checks if the username is already in dicts and checks the regex pattern for the password
# if both are okay initializes a variable that is equal to a new object of the user class and adds him to the dictionary
# flips the crrent_signed_in_user flag

# SIGN OUT
def sign_out():
    global current_signed_in_user
    current_signed_in_user = None
    print('Signing you out...')

# DISPLAY ALL USERS
def display_users():
    for user in users:
        print(user)

#VIEW USER DETAILS
# display details for the current signed in user variable  
def view_account_details():
    global current_signed_in_user
    if current_signed_in_user is not None:
        print(f'''
Username: {current_signed_in_user.get_username()}
Password {current_signed_in_user.get_password()}
Books Currently on loan:
''') 
        for book in current_signed_in_user.get_books_loan():
            print(book.title)
    
  
        