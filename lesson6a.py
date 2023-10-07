#python functions
#creating python fn to calculate BMI
#Syntax
#BMI = Weight/height**2

import math
import random


weight = 60
height = 1.8

#defining the fn
def BMI():
    bmi_value = weight / height**2
    #print(f"The BMI Value is {bmi_value}")
    return bmi_value
BMI()

#built in fns

def Square_root():
    number = 81
    square_root = math.sqrt(number)
    print(square_root)
Square_root()

def Random():
    languages=['Kotlin', 'Java', 'Python', 'C']
    random.shuffle(languages)
    print(languages)
Random()
#parameters and arguments
#parameters defined inside the parenthesis when creating a fn
def sum_numbers(number1, number2, number3):
    sumofNumbers = [number1, number2, number3]
    sum_numbers = sum(sumofNumbers)
   # print(f"The sum of the numbers is {sum_numbers}")
    return sum_numbers
sum_numbers(10,2,3)

#return value: addition of three numbers
addition = sum_numbers(5,3,2)
print(addition)

print("My BMI value is", BMI())


