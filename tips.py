import sys
from collections import Counter

generator = (i for i in range(10))
list = [i for i in range(10)]
print(f"Type{generator}", generator)
# for i in generator:
#     print(i)

print("Sum of list", sum(list))

print(sys.getsizeof(generator, "bytes"))
print(sys.getsizeof(list, "bytes"))


data = [2, 4, 9, 0, 1, 3, 5, 7, 1, 1, 1, 1, 6, 9, 9, 8, 9, 1]
sorted_data = sorted(data, reverse=True)
print(f"data: {data} \nsorted data: {sorted_data}")

#Sorting can be done by calling sort() on list too.
copy_data = data = [2, 4, 9, 0, 1, 3, 5, 7, 1, 1, 1, 1, 6, 9, 9, 8, 9, 1]
copy_data.sort(reverse=True)
print("Sorted : copy_data: ", copy_data)

counter = Counter(data)
print(counter)
#Pass an item to counter to get its count
print(counter[1])
#To get most common item, use most_common() method
#This will return a list of tuple
# arg 1 will return mc item and arg 2 will return second most common item too.
most_common = counter.most_common(1)
second_most_common = counter.most_common(2)
print(most_common)
print(second_most_common)

#To access this elements or values, 0 picks first element which is a tuple, and then second 0 picks values
print(f"Most common item is : {most_common[0][0]}\nMost common item appears {most_common[0][1]} times")

name = "Farhad"
print_msg = f"Hello, {name}"
print(print_msg)
i = 2
squared = f"{i} square of {i} is {i*i}"
print(squared)

list_of_strings = ["Hello,", "welcome", "to", "Chittagong"]
concat_strings = " ".join(list_of_strings)
print(concat_strings)

YEAR = 2022
print('Year is {}'.format(YEAR))

