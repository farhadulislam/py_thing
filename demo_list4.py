veg_items = ['Onions', 'Garlic', 'Tomatoes', 'Cabbage', 'Cauliflower', 'Aubergine', 'Raddish', 'Beans']
list_nums = [9, 8, 5, 0, 34, 55, 2, 1, 3, 5, 6, 9]
#sorting
veg_items.sort()
list_nums.sort()
print(veg_items)
print(list_nums)

veg_items.reverse()
list_nums.reverse()
print(f" After reversing items : {veg_items}")
print(f" After reversing items : {list_nums}")

fruits = ['apple', 'banana', 'mango', 'papaya']
print(fruits)
#append takes just one argument
fruits.append('kiwi')
print(fruits)
fruits.insert(0, 'pineapple')
print(fruits)

del_item = 'coconut'
if del_item in fruits:
    fruits.remove(del_item)
else:
    print(f"{del_item} not found in fruits list : {fruits}")

print(fruits)
fruits.pop(1)
print(fruits)

for fruit in fruits:
    del(fruits[0])

if not fruits:
    print('List is empty')
else:
    print('list not empty')

print(f"FRUITS : {fruits}")

del(fruits[0])
print(fruits)
del(fruits[0])
print(fruits)


#appending list to another list

list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 6, 7, 8, 9]

list_1.extend(list_2)
print(list_1)

letters = ["a", "b", "c"]
string = "".join(letters)
print(string)
string = " ".join(letters)
print(string)


list_even=[]