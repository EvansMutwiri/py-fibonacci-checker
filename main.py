from math import sqrt


def isPerfectSquare(num):
    s = int(sqrt(num))
    # if (s * s == num): print('true')
    # else: print('false')
    return s * s == num


def fiboCheck(num):
    if (isPerfectSquare(5 * num * num + 4 or 5 * num * num - 4)):
        print(str(num) + " is in fibo")
    else:
        print("not in fibo")


fiboCheck(int(input("Enter number: ")))
