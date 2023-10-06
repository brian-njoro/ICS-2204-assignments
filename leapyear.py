#Brian Njoroge Irungu -- SCT211-0507/2021

year_str = input("Enter year:")

try:
    year = int(year_str)

    def check_leap_year(year):
        if (year % 4 == 0): #check for remainder
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")

    check_leap_year(year)
except ValueError:
    print("Invalid input. Please enter a valid year.")
