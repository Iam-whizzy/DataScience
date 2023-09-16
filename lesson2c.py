# Numbers : Arithmetics -> Integers, Floats, Complex Numbers
#Integers: Values without decimal places

age = 36
print(type(age))

#Floats:
distance = 20.6
print(type(distance))

#inputing values to the Systen
#We use input("instructions")
#String -> input()
#Integer -> int(input("Instructions"))
#Floats -> float (input("Instructions"))

#Simple Interest
#Principal -> int
#Rate -> float
#time -> int

try:
    name = str(input("Please Enter you Name"))
    principle = int(input("Please Enter your Principle"))
    rate = float(input("Please Enter the Rate"))
    time = int(input("Please Enter the Time"))

    interest = principle * rate * time
    print (f"The interest is {interest}")
except: 
    print("Something went wrong.....")

#Exception Handling try--catch block
