class Book:
    def __init__(self, title, author, genre,):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = True
        self.__borrower = []

    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author
    def get_author(self):
        return self.__author

    def set_genre(self, genre):
        self.__genre = genre
    def get_genre(self):
        return self.__genre

    def set_availablity(self, available):
        self.__available = available
    def get_availablity(self):
        return self.__available

    def set_borrower(self, borrower):
        self.__borrower.append(borrower)
    def get_borrower(self):
        return self.__borrower
    def rm_borrower(self):
        self.__borrower.pop()

    def display_info(self):
        pass

class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.borrowed_books = []

    def set_member_id(self, member_id):
        self.__member_id = member_id
    def get_member_id(self):
        return self.__member_id

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.set_availablity('False')
        book.set_borrower(self.get_member_id())
        print(f"{self.get_member_id()} borrowed \'{book.get_title()}\'")

    def return_book(self, book):
        book.set_availablity('True')
        book.rm_borrower()
        self.borrowed_books.remove(book)


    def display_borrowed_books(self):
        print(f"Books borrowed by \'{self.get_member_id()}\':")
        for b in self.borrowed_books:
            print(f"Title: {b.get_title()} \nAuthor: {b.get_author()} \nGenre: {b.get_genre()} \nAvailable: {b.get_availablity()}")
            print("----------")

class Library:
    def __init__(self):
        self.books_available = []
        self.library_members = []
        print("Welcome to the library!")

    def add_book(self, *books):
        for book in books:
            if book not in self.books_available:
                self.books_available.append(book)
                print(f"\'{book.get_title()}\' added in the library")

    def add_library_member(self, *members):
        for member in members:
            if member not in self.library_members:
                self.library_members.append(member)
                print(f"\'{member.get_name()}\' added as library member, ID: {member.get_member_id()}")

    def display_book_list(self):
        for b in self.books_available:
            print(f"Title: {b.get_title()} \nAuthor: {b.get_author()} \nGenre: {b.get_genre()} \nAvailable: {b.get_availablity()} \nBorrowed by: {b.get_borrower()}")
            print("----------")


    def display_library_members(self):
        pass


b1 = Book("1984", "George Orwell", "Dystopian Fiction")
b2 = Book("To Kill a Mockingbird", "Harper Lee", "Bildungsroman")
b3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Tragedy")
print("1=================================================")
m1 = LibraryMember("LM001", "Robin")
m2 = LibraryMember("LM002", "Ana")
m3 = LibraryMember("LM003", "Palloma")
print("2=================================================")
lib = Library()
#Welcome to the library!
print("3=================================================")
lib.add_book(b1, b2, b3)
#b.title added
print("4=================================================")
lib.add_library_member(m1, m2, m3)
#Welcome to the library, m
print("5=================================================")
m1.borrow_book(b1)
m1.borrow_book(b2)
m3.borrow_book(b3)
print("6=================================================")
lib.display_book_list()
# Title: XYZ
# Author: abc
# Genre: pqr
# Available: T/F
# Borrowed by: id
#----------------
print("7=================================================")
m1.display_borrowed_books()
# Books borrowed by m1:
# Title: Harry Potter and the Chamber of Secrets
# Author: J.K. Rowling
# Genre: Fiction
# Available: False
print("8=================================================")
m1.return_book(b1)
lib.display_book_list()
print("9=================================================")
m1.display_borrowed_books()
# Books borrowed by m1:
# Title: Harry Potter and the Chamber of Secrets
# Author: J.K. Rowling
# Genre: Fiction
# Available: False
print("9=================================================")
