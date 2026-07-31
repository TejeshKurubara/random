class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        self.books.append(Book(book_id, title, author))
        print("Book Added Successfully!")
    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available")
            return
        print("\nBook ID\tTitle\tAuthor\tStatus")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(book.book_id, "\t", book.title, "\t", book.author, "\t", status)
    def search_book(self):
        title = input("Enter Book Title: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found")
                print("Book ID :", book.book_id)
                print("Title   :", book.title)
                print("Author  :", book.author)
                return
        print("Book Not Found")
    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        self.members.append(Member(member_id, name))
        print("Member Registered Successfully!")
    def display_members(self):
        if len(self.members) == 0:
            print("No Members Registered")
            return
        print("\nMember ID\tName\tBorrowed Books")
        for member in self.members:
            print(member.member_id, "\t\t", member.name, "\t", member.borrowed_books)
    def borrow_book(self):
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is None:
            print("Member Not Found")
            return
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    member.borrowed_books.append(book.title)
                    print("Book Borrowed Successfully")
                else:
                    print("Book Already Borrowed")
                return
        print("Book Not Found")
    def return_book(self):
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is None:
            print("Member Not Found")
            return
        for book in self.books:
            if book.book_id == book_id:
                if book.title in member.borrowed_books:
                    member.borrowed_books.remove(book.title)
                    book.available = True
                    print("Book Returned Successfully")
                else:
                    print("This member did not borrow this book.")
                return
        print("Book Not Found")
library = Library()
while True:
    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. Display Members")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.display_books()
    elif choice == 3:
        library.search_book()
    elif choice == 4:
        library.add_member()
    elif choice == 5:
        library.display_members()
    elif choice == 6:
        library.borrow_book()
    elif choice == 7:
        library.return_book()
    elif choice == 8:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")