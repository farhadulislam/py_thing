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

