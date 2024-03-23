#Initialize two data structures to keep track of books and members both represented as lists
book = []
member = []

#appends a new book dictionary to the books list.
book.append({
        "book_id": 2024001,
        "title": "Python Programming",
        "author": "Jacob Zuma"
        })

member.append({
        "member_id": 1,
        "name": "Anelisa Maleka",
        })

#Display
print("Books ", book)
print("\nMembers ", member)