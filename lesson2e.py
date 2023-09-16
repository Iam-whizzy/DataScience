#LIST DDATA TYPES: Used to store collection of values on the same variable

#Bad Scenario
county1 = "Nairobi"
county2 = "Bomet"
county3 = "Samburu"

#Best Scenario
counties = ["Nairobi", "Bomet", "Samburu"]
years = [2015, 2019, 2021, 2023]
student = ["Jane", 21, False, 15000.00, ["0791234567", "0786234567"]]
print (type(counties))

#Properties of a list: Uses sq brackets [], items comma separated
#other properties: Ordered(indexing), Modifiable/ Changeable, Allows Duplicates

#Ordering: Each item is given an index value starting from zero[]
print(counties[0])

#Accessing a nested List
print(student[4][1])

#Task:
customer = ['Derrick', ["Nairobi", 'Kisumu', 'Kilifi'],['derrick69@gmail.com', ['0701234567', '0786112345']]]
#Using Indexing:
#a) Access the email
#b) Access all the contacts
#c) Access Kisumu

print(customer[1][1])
print(customer[2][0])
print(customer[2][1][0])

tensors = [[1,2], 3, [4,[5,6,[7,8]]]]
#Access 6, 8, 3

print(tensors[2][1][1])
print(tensors[2][1][2][1])
print(tensors[1])

#RANGE 
# ADD AN ITEM 
# ADD AN ITEM AT POSITION 
# REPLACE/UPDATE 
# DELETE AN ITEM 
# DELETE AN ITEM AT SPECIFIC POSITION