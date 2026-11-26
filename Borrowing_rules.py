# all input details
book_name = input("Please enter which book you need to borrow -")
age = int(input("please enter your age -"))
borrrowed = int(input("How many books have you already borrowed -"))
book_name = book_name.capitalize


book_available = {"Spider"  : "available"  , "Wings" : "borrowed "," marvel " : "available ", " avengers" : "borrowed", " comic" : "available"}

for book_name in book_available:
    if book_available[book_name] == "available":

        if(borrrowed < 3): # a user can only borrow 3 books 
            if age >= 18 or borrrowed < 2:
                print('You are eligible for borrowing') # 18 and <2
            else:
                print("You must be atleast 18 to borrow a book and already borrowed is less than 3 ")
            
        else:
              print("We do not allow more borrowing")
    else:
            print("Book is unavilable") # name not found









 

