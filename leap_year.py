year = input("Please enter a year:")

year = int(year)

if year % 100 != 0 and year % 4 == 0:

    print(year, "Yes! This year is a leap year.")

elif year % 100 == 0 and year % 400 == 0:

    print(year, "Yes! This year is a leap year.")

else:

    print(year, "No! This year is not a leap year.")


