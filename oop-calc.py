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