#DICTIONARIES: Stored in key - value pair
#Syntax: curly braces -> {}
#Properties: unordered, no duplicates, changeable/ mutable

#{key(left) -> string : value(right) -> any data type }

student ={
          'first_name': 'Eric',
          'age': 37,
          'course': 'Data Scienc',
          'GPA': 3.17,
          'Subjects': ['Python','Stats', 'ML', 'AI']            
}
print(type(student))

#Operations
#1. Accessing Items
#We use key to acess values

print(student['age'])

#Access the subjects
print(student['Subjects'])

#Add a new subject: 'DL'
student['Subjects'].append('DL')
print(student['Subjects'])

#1.Add new items: the key should be unique, otherwise its a duplicate
student['has_completed'] = False
print(student)

#2. Update(We use an already existing key and assign it a new value)
student['age'] = 40
print (student)

#3. Delete a pair
student.pop("first_name")
print(student)

#clear all items in a dictionary
student.clear()
print(student)

#NB: Lookup dataframes & Series
#Uses Lists and Dictionaries



