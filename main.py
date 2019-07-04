# Homework 4 by Ru Meng(Dan) Wang main.py

n = input("Enter a year greater than or equal to 1582 to evaluate (enter -1 to exit the program): ")
year = int(n)

while(year!=-1):
    if year < 1582:
        print("Invalid Input!")
    else:
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    print("The year is a leap year (it has 366 days).")
                else:
                    print("The year is NOT a leap year (it has 365 days).")
            else:
                print("The year is a leap year (it has 366 days).")
        else:
            print("The year is NOT a leap year (it has 365 days).")

    n = input("Enter a year greater than or equal to 1582 to evaluate (enter -1 to exit the program): ")
    year = int(n)

print("Goodbye!")
