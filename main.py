from math import sqrt


def isPerfectSquare(num):
    s = int(sqrt(num))
    return s * s == num


def fiboCheck(num):
    if (isPerfectSquare(5 * num * num + 4 or 5 * num * num - 4)):
        print(str(num) + " is in Fibonacci series")
    else:
        print(str(num) + " is not in Fibonacci series")


fiboCheck(int(input("Enter number: ")))
