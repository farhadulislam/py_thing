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

#kwargs  = parameters that pack all arguments into a dictionary

def greet(**kwargs):
    print('Hello', end = " ")
    for key,value in kwargs.items():
        print(value, end = " ")

greet(f="James", l="Bond")

def printItems (**kwargs):
    print(kwargs)
printItems(a = 1, b = 2, c = 3)


''' Key word argument are a way to pass arguments to a function preceded by keyword'''
def sayHello(first, middle, last):
    print("Hello, {} {} {} ".format(first, middle,  last))

sayHello(last ="Islam" , first = "Md", middle = "Farhad" )

