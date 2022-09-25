import random

x = random.randint(1,6)
y = random.random()

print(f"{x}, {y}")
computer_choice = random.choice(['rock', 'paper', 'scissor'])
user_choice = input("Please, enter your choice from below \nROCK | PAPER | SCISSOR\n")
print("User choice is {}".format(user_choice))
print(f"Computer choice is : {computer_choice}")
if user_choice.lower() == computer_choice:
    print("Drawn")



item_costs = [1, 2, 3, 4, 5, 50, 60, 70]
shopping_list = ["Potatoes", "Rice", "Onions", "Oil", "Flour", "Chilli", "Garlic", "Ginger"]
random.shuffle(shopping_list) # Ensure, you run shuffle methond first, then print the actual list.
random.shuffle(item_costs)
print("Shuffled items {} {}".format(shopping_list, item_costs))


