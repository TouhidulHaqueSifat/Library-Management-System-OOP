class Library:
    
    def __init__(self, libraryName):
        self.name = libraryName
        self.students = []
        self.teachers = []
        self.books = []

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



    