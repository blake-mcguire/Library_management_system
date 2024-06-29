
class Author:
    
    def __init__(self, name, biography):
        self.__name = name 
        self.__biography = biography
        self.__genres = []
        self.__books = []        
        
    def get_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography

    def set_biography(self, new_bio):
        self.__biography = new_bio
    
    def get_genres(self):
        return self.__genres
    
    def add_to_genres(self, new_genre):
        if new_genre not in self.__genres:
            self.__genres.append(new_genre)
        else:
            print(f'The genre is already assocaited with this author!')
    def get_books(self):
        return self.__books
    
    def add_book(self, new_book):
        if new_book not in self.__books:
            self.__books.append(new_book)
    
authors = []
def author_exists(author_name):
    pass     
        


def add_author():
    author_name = input('What is the name of the author?: ').title()
    bio = input('Write a short bio about this author: ')
    try:
        if author_exists(author_name):
            print(f'That Author already exists in out library.') 
            return
        else:
            new_author = Author(author_name, bio)
            authors.append(new_author)
            print(f"Added new Author: {author_name}")   
    except Exception as e:
        print(e)


def search_author():
   name_search = input('Enter the name of the author you would like to find: ')
   found = False
   for author in authors:
       if author.get_name() == name_search:
           print('Author Found!')
           print(f"Name: {author.get_name()}")
           print(f"Biography: {author.get_biography()}")
           print(f"Works: {', '.join(author.get_books())}")
           print(f"Noteable Genres: {', '.join(author.get_genres())}")
           found = True
           break
   if not found:
        print('Author not found!')
        
def view_authors(authors):
    if not authors:
        print('We currently have no authors!')
    else:
        try:  
            for author in authors:
                print(f'~ {author.get_name()}')
        except Exception as e:
            print(e)