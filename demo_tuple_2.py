import sys
import timeit

my_tuple = (1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10)
my_list = list(my_tuple)

print(f"{type(my_tuple)}")
print(sys.getsizeof(my_tuple), "bytes")
print(sys.getsizeof(my_list), "bytes")

num1, *rest, num2 = my_tuple
print(rest)

print(f"Printing every second item from tuple {my_tuple[::2]}")
print(f"Reversing the tuple :  {my_tuple[::-1]}")

print(timeit.timeit(stmt="(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)", number=100000))
print(timeit.timeit(stmt="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", number=100000))

print(my_tuple.count(3))
print(my_tuple.index(9))
print(len(my_tuple))

multi = ('python',)*3
print("Mulitiplied tuple", multi)

tuple_from_tuple_contructor = tuple("Apple")
print(tuple_from_tuple_contructor)
