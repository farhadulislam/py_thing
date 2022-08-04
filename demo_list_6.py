import itertools

list0 = ['one', 'two', 'three', 'four', 'five']
list1 = [1, 2, 3, 4, 5, 50, 60, 70]
list2 = ['orange', 'mango', 'jackfruit', 'watermelon', 'grapes']
list4 = [2, "Hathazari", 3, "Panchlaish", 4, "Rangunia", 5, "Raozan"]

list_all = list(zip(list0, list1, list2))
print(list_all)
for i in list_all:
    print(list(i))


mishkat_tuple = (20, 30, 40, 50, 50, 50, 50, 50, 50)
miskat_set = set(mishkat_tuple)

print(f"Mishkat's tuple : {mishkat_tuple}")
print(f"Mishkat's set : {miskat_set}")

names = ["Bahar", "Raisul", "Sabuj"]
ages = [31, 34, 40]
eye_colours = ["Green", "Black", "Blue"]

n_a_e = list(zip(names, ages, eye_colours))
print(n_a_e)

for name, age in zip(names, ages):
    if age < 35:
        print(name)

sum = itertools.accumulate(list1)
print(list(sum))

#Sorting list elements

numbers = [[4,5],[0,2],[9,-3],[2,8]]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort(key=lambda x: x[0] + x[1])
print("Sort by sum of elements\n", numbers)
numbers_2 = [[4,5],[2,],[3,4,5,6], [0,2],[9,-3],[2,8], [100,200,2,3,5,6,7]]
numbers_2.sort(key=lambda x: len(x))
print("Sort by number of elements or length\n", numbers_2)

list_from_sums = [i[0] + i[1] for i in numbers]
print(list_from_sums)

#Form a list of two lists - first containing 1st element of each list item,
#and second containing 2nd element of each list items
unpack_numbers = [[i[0] for i in numbers], [i[1] for i in numbers]]
print(unpack_numbers)
unpack_numbers[0].sort()
unpack_numbers[1].sort()
print(unpack_numbers)

print(list4)




