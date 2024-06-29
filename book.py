import user
import author
# import genre

library = {}
current_loans = {}

class Book:
    def __init__(self, title, genre, author):
        self.__title = title
        self.__genre = genre
        self.__author = author
        self.__is_available = True
        
    def get_title(self):
        return self.__title
    
    def get_genre(self):
        return self.__genre
    
    def get_author(self):
        return self.__author
    
    def get_availability(self):
        return self.__is_available
    
    def set_availability(self):
        if self.get_availability:
            self.__is_available = False
        else:
            self.__is_available = True
    def borrow_book(self):
        if self.get_availability():
            self.set_availability()
            return True 
        return False
    
    def return_book(self):
        self.set_availability()
        

def add_book():
    title = input('Enter the title of the book you would like to add!: ').title().strip()
    author_name = input('Who wrote the book?: ').title().strip()
    genre_name = input('what is the genre?: ').title().strip()
    new_book = Book(title, genre_name, author_name)
    
    existing_author = next((a for a in author.authors if a.get_name() == author_name), None) 
    
    if existing_author:
        if title in existing_author.get_books():
            return
        else:
            existing_author.add_book(title)
        if genre_name not in existing_author.get_genres():
            existing_author.add_to_genres(genre_name)
    else:
        new_author = author.Author(author_name, f'Author of the {genre_name} genre.')
        new_author.add_book(title)
        new_author.add_to_genres(genre_name)
        author.authors.append(new_author)


        
    library[title] = new_book
    print(f'{title}, has been added to the library. Thank you for your donation!')
    
    


def borrow_book():
    book_choice = input('Enter the name of the book you would like to borrow: ')
    if book_choice in library:
        book = library[book_choice]
        if book.get_availability():
            book.borrow_book()
            current_loans[book_choice] = user.current_signed_in_user.get_username()
            user.current_signed_in_user.add_book_to_loans(book_choice, book)
            print(f"{book_choice}, has been added to your collection!")
        else:
            print(f'Sorry, {book_choice} is currently not available')
    else:
        print('Sorry we dont carry that book!')

def return_book():
    books_loaned = user.current_signed_in_user.get_books_loan()
    if books_loaned:
        try:
            print('Books Currently Loaned to you:')
            for title in books_loaned:
                print(f'~~ {title}', end='')
                book_to_return = input('\nWhich Book Would you like to return: ')
                if book_to_return in books_loaned:
                    user.current_signed_in_user.remove_book_from_loans(book_to_return)
                    
                    if book_to_return in current_loans:
                        del current_loans[book_to_return]
                    library[book_to_return].set_availability()
                    print(f'{book_to_return}, has been returned. Thank You!')
                else:
                    print('That book isnt loaned to you at the moment!')
        except Exception as e:
            print(e)
    else:
        print('You dont have any books currently loaned to you from us!')

def search(library):
    title = input('What is the title you are looking for? ')
    if title in library:
        book = library[title]
        print('book found ')
        print(book.get_title())
        print(book.get_genre())
        print(book.get_author())
        print(book.get_availability())
    else:
        print('Sorry that book is not in our library!')
                        

def display_books(library):
    for book in library.values():
        
        print(f'{book.get_title()}, by {book.get_author()}: {book.get_genre()}. Available:{book.get_availability()}')