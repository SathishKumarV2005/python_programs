class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"Book:{self.title} \nAuthor: {self.author} \nPages: {self.pages} pages\n"

# Creating three book objects
book1 = Book("Ponniyin Selvan", "Kalki", 2210)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 228)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

# Printing descriptions
print(book1.description())
print(book2.description())
print(book3.description())
