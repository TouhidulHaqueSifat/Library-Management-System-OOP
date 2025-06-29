from models.books import *
from models.library import *
from models.user import *

def main():
    # Create library
    
    lib = Library("SCH")

    # Add books
    b1 = Book("1984", "George Orwell", "123")
    b2 = Book("The Hobbit", "J.R.R. Tolkien", "456")
    lib.addBook(b1)
    lib.addBook(b2)

    # Register users
    u1 = Student("Alice")
    lib.registerUser(u1)

    t1 = Teacher("Sam")
    lib.registerUser(t1)

    


    # Show books
    lib.isAvailble()

    # Borrow and return flow
    book_to_borrow = lib.findBook("1984")
    if book_to_borrow:
        u1.borrowBook(book_to_borrow)

    lib.isAvailble()

    u1.returnBook(book_to_borrow)
    lib.isAvailble()

    for user in lib.students:
        print(user.name)

    for user in lib.teachers:
        print(user.name)

    book_to_borrow = lib.findBook("The Hobbit")
    if book_to_borrow:
        t1.borrowBook(book_to_borrow)
    
    lib.book_review(b1)
    print(lib.bookReviews)
    lib.showReview(b1.title)
    

    print(t1._id)

if __name__ == "__main__":
    main()