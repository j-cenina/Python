def leap_year():
    year = int(input("Enter a year to determine if its leap year or not: "))
    if year % 4 == 0 or (year % 100 and year % 400) == 0:
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))
leap_year()

