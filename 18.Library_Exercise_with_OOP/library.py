class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.available = True
    
    ##This line is to make a list can be read as a string and not like an object
    ##This is first
    def __str__(self):
        return f'{self.title} by {self.author}'
    ##This is second
    def __repr__(self):
        return self.__str__()
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'The book {self.title} is borrowed')
        else: 
            print(f'The book {self.title} is already borrowed')        
    
    def return_book(self):
        self.available = True
        print(f'The book {self.title} has been returned')


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.user_books = []

    def user_borrow(self, book):
        if book.available:
            self.user_books.append(book)
            book.available = False
            print(f'The customer {self.name} with id {self.id} has borrowed the book {book.title} and now the users books are {self.user_books}')
        else:
            print(f'This book {book.title} is not available')
    def user_return(self, book):
        if not book.available:
            self.user_books.remove(book)
            book.available = True
            print(f'You have succesfully returned the book {book.title}')
        else:
            print(f'You dont have this book {book.title} to return, you have {self.user_books}')

class Library():
    def __init__(self):
        self.books = []
        self.users = []

    def add(self, book):
        if book in self.books:
            print("Book is already added")
        else:
            self.books.append(book)
            print(f'The book has been added')    

    def register(self, user):
        if user in self.users:
            print("The user is already registered")
        else:
            self.users.append(user)
            print("The user is registered")

    def bookavailable(self, book):
        print(f'Libros disponibles {self.books}')
        if book in self.books:
            if book.available: 
                print(f'The book {book.title} by {book.author} is available')
        else:
            print(f'The book {book.title} is not available, please add it')



book1 = Book("Andres", "The programmer")
book2 = Book("David", "The cooker")

user1 = User("Melodie", "001")
user2 = User("Angie", "002")



# We create the library
example_library = Library()
example_library.add(book1)
example_library.add(book2)

example_library.bookavailable(book1)


user1.user_borrow(book1)
user2.user_borrow(book1)

user1.user_return(book1)
user1.user_borrow(book2)

user2.user_borrow(book1)