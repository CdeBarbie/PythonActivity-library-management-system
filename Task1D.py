#Rewrite the entire Task 1 C using Data frames instead of lists.
import pandas as pd

book = {'book_id':[2024001], 'title':['Python Programming'], 'author':['Jacob Zume'], 'status': ['Avaliable']}
df = pd.DataFrame(book)
print("Book dataframe: ", df, "\t")

member = {'member_id': [1], 'name':['Anelisa Maleka'], 'borrowed_book': [5]}
memberDF = pd.DataFrame(member)
print("\nMember dataframe: ", memberDF, "\t")
