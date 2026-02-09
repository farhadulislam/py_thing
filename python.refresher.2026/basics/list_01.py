def print_me(x):
    #if (len(x) ==0):
       # print("WRONG INPUT")
    print(f"INPUT TYPE {type(x)}\nPRINTING: {x}")

#list of fruits
list_fruit = ["apple", "banana", "carrot"]
print(f"list_fruit: {list_fruit}")
print(list_fruit.count("jamboora"))
if "jamboora" not in list_fruit:
    list_fruit.append("jamboora")
print_me(list_fruit)

#Adding numbers to a list
list_numbers = []
for i in range(10):
    list_numbers.append(i)

print_me(list_numbers)
print_me(1)


#Insert at given position
print_me("insert at a given position")
list_fruit.insert(0,"coconut")
list_fruit.insert(len(list_fruit),"amloki")
print_me(list_fruit)

#Delete safely
if 'pineapple' not in list_fruit:
    print("Item Not found in the list")
else:
    list_fruit.remove('pineapple')

if 'coconut' not in list_fruit:
    print("Item Not found in the list")
else:
    list_fruit.remove('coconut')
print_me(list_fruit)

list_fruit.sort()
print_me(list_fruit)
list_fruit.reverse()
print_me(list_fruit)
