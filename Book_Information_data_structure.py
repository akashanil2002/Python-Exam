library_name = "College_Library"
number_of_books = 5
library_open = True

books = ["Spider", "Wings"," marvel ", " avengers", " Angles"] # store 5 books as a list 
books_catgory = ("comic", "comedy", "story", "life lessons", ) # book categories in tuple

#display library details
print("library name is", library_name )
print("Number of books in library ", number_of_books)
print("Is library open ", library_open)
print("all books details", books)
print("All book category avalable", books_catgory)

#book names and their availability status
book_available = {"Spider"  : "Available"  , "Wings" : "borrowed "," marvel " : "Available ", " avengers" : "borrowed", " comic" : "Available"}
Available = 0 
borrowed = 0

print("The Availability of the books:")

for book in book_available:
    if book_available[book] == "Available":
        Available = Available + 1
    else:
        borrowed = borrowed + 1

#display number of books avalable and borrowed
print("The number of books available", Available)
print("The number of books borrowed ", borrowed)
