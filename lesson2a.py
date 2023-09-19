print ("Hello World")
print ("Welcome to Python for Data Science")

#Ignored
#Variables: Stored Values
course = "Artificial Intelligence"
cost = 200000

print (course, cost)
print(f"The {course} course will cost you KES {cost}")

#operators: Symbols or keywords used to perform operations
#Arithmetic: +, -, /, *
#Comparison operators: (<, >, <=, >=, ==, !=)
#They are used to check the relationship between variables/ values(they form conditions) - alt + Z for line break, they return two instances(True or False)

variable1 =  100
variable2 = 200
print(variable1 > variable2)
print(variable1 < variable2)
print(variable1 <= variable2)
print(variable1 >= variable2)
print(variable1 == variable2)
print (variable1 != variable2)

#Simple Login System
registered_password = "user@123"
user_password = "123"

registered_username = "admin"
received_username = "admin"
print(registered_password == user_password)
print(registered_username == received_username)

#Logical Operators: and, or, not
#Used to check relationship between condition
#and: Return True only when both conditions return True, otherwise False
#or : Returns True, when atleast one condition is True, but returns False when both are false

print(registered_username == received_username and not registered_password == user_password)


