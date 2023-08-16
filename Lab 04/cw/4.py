#4
class Author:
    def __init__(self, name=None):
        self.name = name
        self.books = {}

    def setName(self, name):
        self.name = name

    def addBook(self, title, genre):
        if self.name is None:
            print("A book cannot be added without an author name")
            return

        if genre not in self.books:
            self.books[genre] = []

        self.books[genre].append(title)

    def printDetail(self):
        print(f"Number of Book(s): {len(self.books)}")
        print(f"Author Name: {self.name}")
        for genre, titles in self.books.items():
            print(f"{genre}: {', '.join(titles)}")

# Do not change the following lines of code.
a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon","Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")
