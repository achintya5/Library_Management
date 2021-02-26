# create a library class
# define methods to display all books,
# lend books, donate books and
# return books

# create a dictionary to store the name of the book borrowed and the person who has borrowed it.

class Library:
    def __init__(self, books, lib_name):
        self.books = books
        self.lib_name = lib_name

    def book_see(self):
        return f"The books in {self.lib_name} are \n{self.books}"

    def book_add(self, donation):
        self.donation = donation
        self.books.append(donation)
        if donation in book_dict:
            print("Thank you, but we already have that book!")
        else:
            book_dict[donation] = 21
            print("Thank you for your response!! Your book has been added.")

    def book_borrow(self, choice, name):
        self.choice = choice
        self.name = name
        if type(book_dict[choice]) == int:
            print("The book is still available\nIssued successfully")
            book_dict[choice] = name
        else:
            print("The book is not available :(\nCheck out our other books!")

    def book_return(self, book_ret, name):
        self.name = name
        self.book_ret = book_ret
        if book_ret in Achintya_lib.books and book_dict[book_ret] == name:
            print("Thank You for returning the book!")
            book_dict[book_ret] = 0
        elif book_ret not in Achintya_lib.books:
            print("No such book found in our server! Please try again")
        else:
            print("The book was borrowed by someone else!")


Achintya_lib = Library(["book1", "book2", "book3", "book4", "book5", "book6",
                        "book7", "book8", "book9", "book10", "book11", "book12",
                        "book13", "book14", "book15", "book16", "book17", "book18",
                        "book19", "book20"],
                       "Achintya Library")

book_dict = {'book1': 1, 'book2': 2, 'book3': 3, 'book4': 4, 'book5': 5, 'book6': 6, 'book7': 7, 'book8': 8,
             'book9': 9, 'book10': 10, 'book11': 11, 'book12': 12, 'book13': 13, 'book14': 14, 'book15': 15,
             'book16': 16, 'book17': 17, 'book18': 18, 'book19': 19, 'book20': 20}

status = "1"
while status == "1":
    name = input('Enter your name here: ')
    purpose = input(
        "Enter 1 if you want to borrow a book\nEnter 2 if you want to donate a book\nEnter 3 if you want to return a book")

    if purpose == "1":
        print(Achintya_lib.book_see())
        choice = input("Enter the name of the book you want ")
        if choice in Achintya_lib.books:
            Achintya_lib.book_borrow(choice, name)
        else:
            print("We don't have that book, check out our other books!")

        status = input("Press 1 if you want to continue\nPress anything else to quit")
    elif purpose == "2":
        donation = input("Enter the book you want to donate: ")
        Achintya_lib.book_add(donation)
        status = input("Press 1 if you want to continue\nPress anything else to quit")
    elif purpose == "3":
        book_ret = input("Enter the book you want to return!!")
        Achintya_lib.book_return(book_ret, name)
        status = input("Press 1 if you want to continue\nPress anything else to quit")
    else:
        print("Please enter a valid number!!")
