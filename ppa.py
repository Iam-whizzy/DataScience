# DICTIONARIES
import calc
person = {
    'firstname': 'John',
    'lastname' : 'Doe' ,
    'age': '69',
    'position' : 'Data Scientist' ,
    'email_address': 'johndoe33@gmail.com',
    'phone_numbers' : ['0701234567', '0789000678']
}
print(person['age'])
print(person['phone_numbers'])

for counter in range(5):
    print(counter)

tensors = [[1,2], 3, [4,[5,6,[7,8]]]]
for tensors in tensors:
    print (tensors)
    
print (calc.add(10, 2))
print (calc.substract(10, 2))


