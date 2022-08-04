'''
We use *args if exact number of arguments passed to function is unknown
and for keywords passed as argument, we use kwargs.
'''

def addition (*args):
    print(f"Arguments passed in {args}")
    total = 0
    for i in args:
        total += int(i)
    return total

if __name__ == "__main__":
    value = addition(0, 1, 2, 4, 5)
    print(f"Value is {value}")

def printItems (**kwargs):
    print(kwargs)

printItems(a = 1, b = 2, c = 3)

