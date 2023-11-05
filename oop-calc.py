#Brian Njoroge Irungu -- SCT211-0507/2021

class Calculator:
    def __init__(self, name):
        self.name = name

    def get_operands(self):
        # Prompt the user for the first operand
        self.num1 = float(input("Enter the first operand: "))
        # Prompt the user for the second operand
        self.num2 = float(input("Enter the second operand: "))

    def get_operation(self):
        # Prompt the user for the operation to be carried out on operands
        self.operation = input("Enter the operation ('+' for addition, '-' for subtraction, '*' for multiplication, '/' for division): ")

    def perform_operation(self):
        # Define functions for the numerical operations
        def addition():
            return self.num1 + self.num2

        def subtract():
            return self.num1 - self.num2

        def multiply():
            return self.num1 * self.num2

        def division():
            if self.num2 == 0:
                raise ValueError("CANNOT DIVIDE BY ZERO!!")
            return self.num1 / self.num2

        # Conditional statement to perform the selected operation
        if self.operation == "+":
            self.result = addition()
        elif self.operation == "-":
            self.result = subtract()
        elif self.operation == "*":
            self.result = multiply()
        elif self.operation == "/":
            self.result = division()
        else:
            self.result = "Invalid operation selected."

    def display_result(self):
        # Print the result using an f-string
        print(f"Hello, {self.name}, the result of your operation is: {self.result}")


name = input("enter your name")
divide_calc = Calculator(name)

divide_calc.get_operands()
divide_calc.get_operation()
divide_calc.perform_operation()
divide_calc.display_result()
