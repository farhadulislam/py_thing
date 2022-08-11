
list = [i**2 for i in range(5)]
print(list)

(MON, TUES, WED, THU, FRI, SAT, SUN) = range(7)
print(SAT)

intVal, boolVal, stringVal = 2, True, "A String"

x = (lambda x : x+3 )(3)
print(x)

map_data = map(lambda x : x*3, range(6))
print(map_data)

#Unpacking tuple
n_tuple = ('Monday', 1989, True)
day, year, is_nested_tuple = n_tuple

nums_squared = [x**2 for x in range(10)]
print(nums_squared)

binary = [2**x for x in range(10) if x > 0]
print(binary)

#
sum(range(5))
#list(range(0, 10, 2))

zeroes = [[0 for _ in range(3)] for _ in range(5)]
print(zeroes)
