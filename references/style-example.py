class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False

        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False

        self.is_borrowed = False
        return True

    def get_details(self):
        return f"{self.title} by {self.author}"


def main():
    book = LibraryBook("The Secret Garden", "Frances Hodgson Burnett")

    print(book.get_details())
    print(book.borrow())
    print(book.borrow())
    print(book.return_book())


if __name__ == "__main__":
    main()
