def leapYearCheck(year):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(str(year) + " is divisible by both 100 and 400")
        else:
            print(str(year) + " is only divisible by 100 but not 400")
    else:
        return year % 4 == 0

year = int(input("Enter year: "))

is_leap = leapYearCheck(year)

if (is_leap):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")
