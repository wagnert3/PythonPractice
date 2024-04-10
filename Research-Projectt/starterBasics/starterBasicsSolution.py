#Team: Wagner e Charliane - WMAD Sr B - 2024
#Research Project: Advanced Topics

# Python for Beginners Class

# Print Hello World
print("Hello, World!")

# Variable Assignments
# Creating a variable and assigning a number
my_number = 10
print("My number is:", my_number)

# Basic Data Types
my_string = "Hello, Python!"
my_int = 20
my_float = 10.5
my_bool = True
print(my_string, my_int, my_float, my_bool)

# Arithmetic Operations
# Add, subtract, multiply, and divide two numbers
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# String Operations
# Concatenate two strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Conditional Statements
# Check if a number is positive or negative
number = -5
if number > 0:
    print("Positive")
else:
    print("Negative")

# Loops
# Use a for loop to print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Use a while loop to increment a variable from 0 to 10
counter = 0
while counter <= 10:
    print(counter)
    counter += 1

# Functions
# Define a function named `add` that takes two parameters and returns their
# sum
def add(x, y):
    return x + y

# Testing the function
print("Sum of 5 and 3:", add(5, 3))

# Exercise 1: Variable Assignments and Operations
# Instructions: Create two variables, assign numerical values, and perform 
# all arithmetic operations
# Solution:
num1 = 12
num2 = 3
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Exercise 2: Simple Calculator with Conditional Statements
# Instructions: Ask the user for two numbers and an operation; perform the operation
# Solution:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    print("Result:", num1 / num2)
else:
    print("Invalid operation")

# Exercise 3: Loop through a List
# Instructions: Create a list of numbers and use a loop to print each element
# Solution:
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Exercise 4: Function that returns the sum of two numbers
# Instructions: Write and test a function that returns the sum of two numbers
# Solution:
# The function `add` defined above can be used for this exercise. Testing has also been shown 
# above.

def sum_of_two_numbers(a, b):
    return a + b

# Test 1
result1 = sum_of_two_numbers(10, 5)
print("Sum of 10 and 5 is:", result1)  # Expected output: 15

# Test 2
result2 = sum_of_two_numbers(-1, 1)
print("Sum of -1 and 1 is:", result2)  # Expected output: 0

# Test 3
result3 = sum_of_two_numbers(2.5, 3.5)
print("Sum of 2.5 and 3.5 is:", result3)  # Expected output: 6.0















print("Class completed successfully!")

# Creating a list
my_list = ["socks", "toys", "books"]

# Accessing list items
print(my_list[1])  # Prints "toys"

# Changing list items
my_list[1] = "games"

# Adding items to the list
my_list.append("candy")

# Removing items from the list
my_list.remove("socks")

# Looping through the list
for item in my_list:
    print(item)
    

# Combining `and`, `or`, `not`
a = 10
b = 5
c = 20

# Check if `a` is greater than `b` AND less than `c`
print(a > b and a < c)  # Outputs: True

# Check if `a` is less than `b` OR `a` is less than `c`
print(a < b or a < c)  # Outputs: True

# Use `not` to reverse the condition
print(not(a > b))  # Outputs: False    
    
    
    
    
    
    
# Bitwise AND
print(5 & 3)  # Outputs: 1 (0101 & 0011 = 0001)

# Bitwise OR
print(5 | 3)  # Outputs: 7 (0101 | 0011 = 0111)
    
    
# Function    
def say_hello():
    print("Hello, Alicia!")   
    
say_hello()    


# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Emily")


















    
    
    
    
    
    