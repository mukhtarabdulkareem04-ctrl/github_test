from optparse import Values
from random import choice


calc_name = ""
name_of_calculator =""

calc_name = "Nexus"
print("Welcome to", calc_name, "\nAllow me to solve maths for you")

print ("Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print()
print("Select an operation")
choice = input("Enter a Number (1-4): ")

if choice == "1":
    num1 = input("Enter number 1: ")
    num1 = float(num1)
    num2 = input("Enter number 2: ")
    num2 = float(num2)

    result = num1 + num2
    print("result =", result)

elif choice == "2":
    num1 = input("Enter number 1: ")
    num1 = float(num1)
    num2 = input("Enter number 2: ")
    num2 = float(num2)

    result = num1 - num2
    print("result =", result)

elif choice == "3":
    num1 = input("Enter number 1: ")
    num1 = float(num1)
    num2 = input("Enter number 2: ")
    num2 = float(num2)

    result = num1 * num2
    print("result =", result)

elif choice == "4":
    num1 = input("Enter number 1: ")
    num1 = float(num1)
    num2 = input("Enter number 2: ")
    num2 = float(num2)

    result = num1 / num2
    print("result =", result)

else:
    print("not available")
    


