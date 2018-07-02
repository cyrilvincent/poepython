class Publisher:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Author:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName= firstName
        self.lastName = lastName

class Media:

    def __init__(self, id, title, price):
        self.id = id
        self.price = price
        self.title = title
        self.publisher = None
        self.authors = []

    def netPrice(self):
        return self.price * 1.2

class Book(Media):

    def __init__(self, id, title, price, nbPage = 0):
        super().__init__(id,title,price)
        self.nbPage = nbPage

    def netPrice(self):
        return self.price * 1.05 * 0.95 + 0.01

class Cd(Media):

    def __init__(self, id, title, price, nbTrack = 0):
        super().__init__(id,title,price)
        self.nbTrack = nbTrack

    def netPrice(self):
        return self.price * 1.05 * 0.95 + 0.01

if __name__ == '__main__':
    p1 = Publisher(0,"ENI")
    a1 = Author(1,"Cyril","Vincent")
    b = Book(2, "Python", 10)
    b.publisher = p1
    b.authors.append(a1)
    print(b.netPrice())





