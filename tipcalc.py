#Brian Njoroge Irungu -- SCT211-0507/2021

total_bill = float(input("Enter total bill amount: "))
tip_percentage = int(input("Enter percentage tip you wish to pay "))
customers = int(input("Enter number of people to split bill: "))

if tip_percentage not in (10,12,15) :
    raise ValueError ("INVALID TIP: Tip percentage can only be 10,12 or 15")
else:
    payable_amount = (((tip_percentage/100) * total_bill) + total_bill) / customers #amount to be paid by each person

print(f"Amount payable by each customer is {payable_amount}")