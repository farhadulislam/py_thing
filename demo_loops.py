
def demo_while():
    number = 0;
    while (number < 10):
        print(f"Number is : {number}")
        number += 1
        if number == 1:
            continue
        if number >= 10:
            break

    number2 = 20
    while (number2 > 0):
        number2 -= 1
        print(f"Number2 is {number2}")


def demo_do_while():

    # There's no do while construct in python; however, while loop can be modified in a way that at least runs once.
    secret_word = "python"
    counter = 0
    while True:
        word = input("Enter secret word").lower()
        counter = counter + 1
        if word == secret_word or word == "":
            break
        elif word != secret_word and counter > 5:
            break

def demo_while_list():
    list_fruits = ["Apple", "Mango", "Jackfruit"]
    while list_fruits:
        print(list_fruits.pop(-1))
    print(f"list_fruits after removal : {list_fruits}")


demo_while()
demo_while_list()
#demo_do_while()


