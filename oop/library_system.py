class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call the base class __init__
        self.file_size = file_size  # Additional attribute for eBook

    def __str__(self):
        return f"E{super().__str__()}, File Size: {self.file_size}KB"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call the base class __init__
        self.page_count = page_count  # Additional attribute for PrintBook

    def __str__(self):
        return f"Print{super().__str__()}, Page Count: {self.page_count}"


# Composition Class: Library
class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book: Book):
        self.books.append(book)  # Add Book, EBook, or PrintBook instance

    def list_books(self):
        for book in self.books:
            print(book)  # Print details of each book