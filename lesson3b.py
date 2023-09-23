#Tuples: Syntax uses parenthesis ->()
#Properties: immutable/ unchangeable, ordered(indexing), allow duplicates

privileges = ("view_users", "generate_receipts", "delete_records")
print(type(privileges))

#create a tuple of single data
names = ("123", 123)
print (names)
print(type(names))

#ordered
print(privileges[1])
