
list_cities =['Amsterdam', 'Milan', 'Barcelona', 'Sharjah', 'Muskat', 'Chicago']

#print all elements
print(list_cities)

print(list_cities[:])

#print last element

print(list_cities[-1])

#print from 1st to last 3rd element. Drop last elements.
print(list_cities[:-2])


#print from 2nd element till last 3rd.
print(list_cities[1:-2])

#start from 4th element and end at 5th. 5 means 6th element, expr stops at one short in below statement.
print(list_cities[3:5])

menu = [['breakfast', 'lunch', 'dinner'],['bread', 'rice', 'fish'], ['tea', 'juice', 'water']]

print(menu[0][0])

print(menu[1][0])
print(menu[2][0])


#print all items using range and len
for i in range(len(menu)):
    print(menu[i])

print(list_cities)
print(* list_cities)
print(menu)
print(* menu)

list_cities.append("Dubai")


print(list_cities)
if 'Abu Dhabi'  not in list_cities:
    list_cities.append('Abu Dhabi')
    print(* list_cities)

#revers items in a list
numbers = [10, 22, 33, 44, 555, 200]
print(numbers)
numbers.reverse()
print(numbers)

#square each element of list using LIST COMPREHENSION
numbers_squared = [x * x for x in numbers]
print(numbers_squared)

#alternative solution of the above

numbers_squared2 = []
for i in numbers:
    numbers_squared2.append(i**2)
print(numbers_squared2)

#Concatenate items of two lists indexwise
list1 = ['M', 'n', 'i', 'Far']
list2 = ['y', 'ame', 's', 'had']
list3 =[i+j for i, j in zip(list1,list2)]
print(list3)

#Concatenate items of two list such that each forms a pair with items from other list.
list3 = ['Hello, ', 'Welcome, ']
list4 = ['Sir', 'Madam']
salutation = [ i + j for i in list3 for j in list4]
print(salutation)

#Remove empty string from a list

list_with_emptyString = ['Apple', 'Banana', 'Carrot', '' ]
print(list_with_emptyString)
list_without_emptyString = list(filter(None,list_with_emptyString))
print(list_without_emptyString)

#Alternative
result = []
for i in list_with_emptyString:
    if i is not '':
        result.append(i)
print(result)

#Write a program to add item 7000 after 6000 in the following Python List
#Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list_of_lists = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list_of_lists[2][2].append(7000)
print(list_of_lists)

#Remove duplicate occurance from a list
list_with_duplicates = [0, 1, 2, 5, 6, 7, 6, 7, 9, 6]
list_without_duplicates = [i for i in list_with_duplicates if i !=6 ]
print(list_without_duplicates)

#Alternative
while 5 in list_with_duplicates:
    list_with_duplicates.remove(5)
print(list_with_duplicates)
