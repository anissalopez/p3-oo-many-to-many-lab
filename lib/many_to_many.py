class Author:
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        royalties = 0
        for contracts in Contract.all:
            if(contracts.author == self):
                royalties += contracts.royalties

        return royalties
    

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.book == self]
    
    def authors(self):
        return [contracts.author for contracts in Contract.all if contracts.book == self]
    
   


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception("royalties must be a number")
        if isinstance (book, Book):
            self.book = book
        else:
            raise Exception("book must be an instance")
        if type(date) == str:
            self.date = date
        else:
            raise Exception("date must be a string")  
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("book must be an instance")
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda x: x.date)


    @classmethod
    def contracts_by_dates(cls):
        return sorted(cls.all, key=lambda x: x.date)
    
Contract.all = []
author = Author("Name")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
contract1 = Contract(author, book1, "02/01/2001", 10)
contract2 = Contract(author, book2, "01/01/2001", 20)
contract3 = Contract(author, book3, "03/01/2001", 30)

assert Contract.contracts_by_date() == [contract2, contract1, contract3]  

print(Contract.contracts_by_date()) 
print(Contract.contracts_by_dates()) 




