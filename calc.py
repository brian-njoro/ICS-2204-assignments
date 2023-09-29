#Brian Njoroge Irungu -- SCT211-0507/2021
# Prompt the user for their name
name = str (input("Enter your name: "))

# Prompt the user for the first operand
num1 = float(input("Enter the first operand: "))

# Prompt the user for the second operand
num2 = float(input("Enter the second operand: "))

# Prompt the user for the operation to be carried out on operands
operation = input("Enter the operation ('+' for addition, '-' for subtraction, '*' for multiplication, '/' for division)")

# Defining functions for the numerical operations
def addition(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError ("CANNOT DIVIDE BY ZERO!!")
    return num1 / num2

# Conditional statement to perform the selected operation
if operation == "+":
    result = addition(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = division(num1, num2)
else:
    result = "Invalid operation selected."

# Print the result using f string
print(f"Hello, {name}, the result of your operation is: {result}")
