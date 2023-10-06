#Age calculator
from datetime import datetime

birth_date = input("Enter date of birth in the format: Year-Month-Day ")
date = datetime.now()
birthday  = datetime.strptime(birth_date, "%Y-%m-%d")
age = date - birthday

#exact age
years = age.days // 365 #divide no. of days by 365
months = (age.days % 365) // 30 #remainder days divided by 30 to get months
days = (age.days % 365) % 30 #remaining days
print(f"Your age is: {years} years, {months} months, and {days} days") #f string to print exact age
