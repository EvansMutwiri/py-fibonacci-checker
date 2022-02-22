def leapYearCheck(year):
    if(year % 100 == 0):
        return year % 400 == 0
    else:
        return year % 4 == 0

year = int(input("Enter year: "))

# print(leapYearCheck(year))

if (leapYearCheck == True):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")
