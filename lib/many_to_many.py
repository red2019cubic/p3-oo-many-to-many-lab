class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)


# This method should return a list of related contracts.

    def contracts(self):
        list_of_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                list_of_contracts.append(contract)
        return list_of_contracts
# This method should return a list of related books using the `Contract` class as an intermediary.

    def books(self):
        list_of_books = []
        for contract in Contract.all:
            if contract.author == self:
               list_of_books.append(contract.book)
        return list_of_books

# This method should create and return a  new `Contract` object between the author and the specified book with the
#  specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

# This method should return the total amount of royalties
#  that the author has earned from all of their contracts.
    def total_royalties(self):
        total_royalties = []
        for contract in Contract.all:
            if contract.author == self:
                total_royalties.append(contract.royalties)
        return sum(total_royalties)


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        list_of_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                list_of_contracts.append(contract)
        return list_of_contracts

    def authors(self):
        list_of_authors = []
        for contract in Contract.all:
            if contract.book == self:
                list_of_authors.append(contract.author)
        return list_of_authors


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_name):
        if not type(author_name) is Author:
            raise TypeError("Author must be an instance Author Class")
        self._author = author_name

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book_value):
        if not type(book_value) is Book:
            raise TypeError("Book must be an instance book Class")
        self._book = book_value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date_value):
        if not type(date_value) is str:
            raise TypeError("Date must be of type string")
        self._date = date_value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, number_of_royalties):
        if not type(number_of_royalties) is int:
            raise TypeError("Royalties must be of type int")
        self._royalties = number_of_royalties

# This method should return all
# contracts that have the same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls):
        list_of_dates = []
        list_of_contracts = []
        list_of_dates = [contract.date for contract in Contract.all]
        list_of_dates.sort()
        for date in list_of_dates:
            for contract in Contract.all:
                if date == contract.date:
                    list_of_contracts.append(contract)
        return list_of_contracts



