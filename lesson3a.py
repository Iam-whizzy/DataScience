#Lists
#Tuples
#Dictionary
#Decision Making

#RANGE ->:
locations = ["Westlands", "Embakasi", "Karen", "Donholm", "Kitengela", "Kasarani"]

#Display all locations starting from the second item [index:]

print (locations[1:])

#Display Data Upto a Certain Position(the last index is always excluded)

print (locations[:2])

#Range with start and end: Emba, Kite

print(locations[1:5])

#Return all the items

print(locations[:])

#Modifiable/ Mutable -> Add, Update, Delete

languages = ['JavaScript', 'Python', 'Java', 'Kotlin', 'PHP']

#Add: C++. C#
#append()
languages.append('C++')
languages.append("C#")

#extend()
#create a new list add

more_languages = ["Ruby", "Go", "Pearl"]
languages.extend(more_languages)

print(languages)

#append(), extend() by default add items to the end of the list
#To add item at a certain position -> insert()
#insert C at position 3

languages.insert(2, "C")

#Update/ Replace (Transformation)

languages[1] = "Python 3"




print(languages)
