#LIBRARY MANAGEMENT SYSTEM

## Purpose
-This project was built as part of the coding temple backend core coursework with the intent of giving us a 
deeper understanding of the concepts of Object Oriented Programming and how to utilize it in our programs to 
employ better modularization and readability within our code.

## Premise
This Program is meant to simulate a mock online library management system via 
the command line interface.

-It allows users to create multiple accounts
-Add and check out books from the library
-and Subsequently return said books. 

Here is a list of the full functionality:

- Adding a new book with all relevant details.
- Allowing users to borrow a book, marking it as "Borrowed."
- Allowing users to return a book, marking it as "Available."
- Searching for a book by its unique identifier (title) and displaying its  details.
- Displaying a list of all books with their unique identifiers.
- Adding a new user with user details.
- Viewing user details.
- Displaying a list of all users.
- Adding a new author with author details.
- Viewing author details.
- Displaying a list of all authors.
- Quitting the application.


## Modules
The functionality of this program is spread into 4 different files and is brought together by the driver code. The Files included are...

1. book.py
2. author.py
3. user.py
4. main.py -- Driver Code
   
This Project is Oriented around 3 main Classes and the objects inside of them...

### 1. Book
   The 'Book' Class is the base of all functionality within the program and allows us to instantiate new book objects
   with each object having 3 attributes (title, genre & author)
### 2. User 
   The User Class allows all functionality that has to do with user accounts.
   with the user class we can instantiate objects with the attributes name, password and the books_on_loan attribute which is initalized to a default value of an empty list
### 3. Author
    The Author Class is heavily tied to the book class and is automatically updated each time a new book is added to either create a new object of the Author class or to update the books or genres associated with an author object. The author object has 4 attributes, name, biography, genres and books which are both set to default values of empty lists  

## HOW TO USE

To begin using this program clone this repository to your local machine.

Once the program has been succesfully cloned onto your machine start
by running the 'main.py' file in the text editor of your choice.

From there you will be guided in your choices by the menu options provided in the CLI.

Promptly follow the directions given on screen to interact with the program.