class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self) -> str:
        return f"Book: {self.title}, {self.author}"


class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self) -> str:
        return f"EBook: {self.title}, {self.author}, {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self) -> str:
        return f"PrintBook: {self.title}, {self.author}, {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        
        if isinstance(book,Book):
            self.books.append(book)
        

    def list_books(self):
        if not self.books:
            return
        
        for index, book in enumerate(self.books,1):
            print(f"{book}")

