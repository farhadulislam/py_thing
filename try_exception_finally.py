
try:
    numerator = int(input("Enter a number to divide "))
    denominator = int(input("Enter a number to divide by "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Can only divide by a number")
else:
    print(result)
finally:
    print("This will always run")