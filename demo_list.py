import random

list_of_fruits = ['apple', 'banana', 'carrot', 'orange']

list_of_colours= ['red', 'orange', 'yellow', 'white']

list_of_list= [list_of_fruits, list_of_colours]

print(list_of_fruits)
print(list_of_colours)
print(list_of_list)
list_combined = list_of_fruits + list_of_colours

print(list_combined)
print('LAST element of list of fruits is : ' + list_of_fruits[-1])

for i in range(len(list_of_fruits)):
    print(list_of_fruits[i])


random_fruit= random.choice(list_of_fruits)
print(random_fruit)

random.shuffle(list_of_fruits)
print(list_of_fruits)


#append items into list

list_of_fruits.append('watermelon')
list_of_fruits.insert(0, 'mango')
list_of_fruits.insert(-1, 'litchi')

#check index of an item in list

print('INDEX of mango : ' + str(list_of_fruits.index('mango')))

if 'jackfruit' not in list_of_fruits:
    list_of_fruits.append('jackfruit')

print(list_of_fruits)