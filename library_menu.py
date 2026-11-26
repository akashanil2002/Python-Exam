
books = ["Spider", "Wings"," marvel ", " avengers", " Angles"] #display all books
book_available = {"Spider"  : "Available"  , "Wings" : "borrowed "," marvel " : "Available ", " avengers" : "borrowed", " comic" : "Available"}
Available = 0 
menu_num = 0

while menu_num != 6:

    print("***** LIBRARY MENU *****")
    print("1. Display All Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Display Borrowed Books")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

if menu_num == 1:
    for book in books: # for loop for display books
        print(book)
elif menu_num ==2:
    book_name = input("please enter the book name")
    book_name = book_name.capitalize
    if books in book_available:
            if book_available[books] == "Borrowed":
                book_available[books] = "Available"
                print("Book is returned ")

            else:
                print("Book is available")

    else:
        print("Invalid book name")

elif menu_num == 3:
    book_name = input("please enter the book name")
    book_name = book_name.capitalize
        

    if books in book_available:

            if book_available[books] == "Borrowed":
                book_available[books] = "Available"
                print("Book returned successfully")

            else:
                print("Book is already available")

    else:
            print("Invalid book name")
elif menu_num == 3:

    print("Borrowed Books:")
    for book in book_available:

        if book_available[books] == "Borrowed":
                print(books)