#performing opeartions on arithmetic operators
#Write a Python program to take two numbers as input and display the result of all arithmetic operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
print("\nArithmetic Operations Results:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'Division by zero error'}")
print(f"{num1} // {num2} = {num1 // num2 if num2 != 0 else 'Floor division by zero error'}")
print(f"{num1} % {num2} = {num1 % num2 if num2 != 0 else 'Modulus by zero error'}")
print(f"{num1} ** {num2} = {num1 ** num2}")
