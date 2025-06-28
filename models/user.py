from abc import ABC, abstractmethod

class User(ABC):
    _id = 0
    def __init__(self, name,role):
        self.name = name
        self.role = role
        User._id += 1
        self.borrowBooks = []

    @abstractmethod   
    def borrowBook(self, book):
        pass

    @abstractmethod
    def returnBook(self, book):
        pass
        


class Student(User):
    
    def __init__(self, name, role="Student"):
        
        super().__init__(name, role)

    def borrowBook(self, book):
        if book.available:
            self.borrowBooks.append(book)
            book.available = False
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")
    
    def returnBook(self, book):
        if book in self.borrowBooks:
            self.borrowBooks.remove(book)
            book.available = True
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} doesn't have '{book.title}'")


class Teacher(User):
    
    def __init__(self, name, role="Teacher"):
        
        super().__init__(name, role)

    def borrowBook(self, book):
        if book.available:
            self.borrowBooks.append(book)
            book.available = False
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")
    
    def returnBook(self, book):
        if book in self.borrowBooks:
            self.borrowBooks.remove(book)
            book.available = True
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} doesn't have '{book.title}'")



