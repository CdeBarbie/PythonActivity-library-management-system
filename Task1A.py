#Initialize two data structures to keep track of books and members both represented as lists
book = []
member = []

#Create two functions
#The add_book function takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list.
def add_book(book_id, title, author, status):
    book.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
        })

#The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionary to the members list
def add_member(member_id, name):
    member.append({
        "member_id": member_id,
        "name": name,
        "borrowed_book": []
        })

#Calling functions 
    add_book(2024001, "Python Programming", "Jacob Zuma", "Avaliable")
    add_member(1, "Anelisa Maleka")

#Displaying
    print("Books ", book)
    print("\nMembers ", member)