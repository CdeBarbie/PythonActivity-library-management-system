#Initialize two data structures to keep track of books and members both represented as lists
book = []
member = []

#Create two functions
#The add_book function and appends a new book dictionary to the books list.
def add_book():
    book.append({
        "book_id": 2024001,
        "title": "Python Programming",
        "author": "Jacob Zuma",
        "status": "Avaliable"
        })
  
def add_member():
    member.append({
        "member_id": 1,
        "name": "Anelisa Maleka",
        "borrowed_books": []
        })

#Calling functions 
add_book()
add_member()

#Displaying
print("Books ", book)
print("Members ", member)