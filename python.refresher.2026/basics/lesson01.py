
def print_sth():
    name=input("Enter a name\n")
    if not name or not name.strip():
        name = input("Name cannot be null . Please, enter a name\n")
    else:
        print(f"Type of the name:{type(name)}")
        print(name)

    number = input("Enter a number\n")

    if number != "" and number.isdigit():
        number = int(number)
        print(f"Type of the number:{type(number)}")
        print(number)
    else:
        print(f"Your entered : {number}")
        number = input("number cannot be empty, null or a string. Please, enter a number\n")

print_sth()


