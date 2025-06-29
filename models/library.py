
class Library:
    
    def __init__(self, libraryName):
        self.name = libraryName
        self.students = []
        self.teachers = []
        self.books = []
        self.bookReviews = {}

    def addBook(self,bookName):
        self.books.append(bookName)
        print(f"Book'{bookName.title}', added to library ")

    def findBook(self,title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None
            

    def registerUser(self, user):
        if user.role == 'Teacher':
            self.teachers.append(user)

        elif user.role == 'Student':
            self.students.append(user)
        else:
            print("Unknown User Type")
        
        print(f"User'{user.name}',as {user.role} is registered ")

    def isAvailble(self):
        print("\nAvailable Books")
        for book in self.books:
            if book.available:
                return book
        return None

    def book_review(self,book):

        review = input("Please give your review: ")
        if book.title not in self.bookReviews:
            self.bookReviews[book.title] = []
        self.bookReviews[book.title].append(review)
        return self.bookReviews[book.title]
    
    def showReview(self, title_str):
        print("All review keys:", [book.title for book in self.bookReviews])

        if title_str in self.bookReviews:
            reviews = self.bookReviews[title_str]
            for i,review in enumerate(reviews, 1):
                print(f"{i}. {review}")
        else:
            print(f"There are no reviews for '{title_str}'.")
        
        
    


    