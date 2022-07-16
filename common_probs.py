import math
def factUsingMath(num):
    return math.factorial(num)

def factUsingRecursion(num):

    if num ==1:
        return 1
    else:
        return num * factUsingRecursion(num-1)

print(factUsingMath(3))

print(f"Fact using recursion S: {factUsingRecursion(3)}")

#Zero division

def divide(x, y):
    try:
        x/y
    except ZeroDivisionError:
        print("Can't divide by Zero")


divide(3, 0)
######### FIBONACCI ################
def fibbonacci_of (n):
    if n in {0,1}:
        return n
    else:
        return fibbonacci_of(n-1) + fibbonacci_of(n-2)

number = 10
print(f"Fibbonacci using recursion {number} is {fibbonacci_of(number)}")

fibbo = [fibbonacci_of(n) for n in range(11)]
print(fibbo)