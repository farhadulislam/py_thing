list = [1, 2, 3, 4, 5]
tuple = (23, 25, 35, 3, 4, 5)

set_from_list = set(list)
set_from_tuple = set(tuple)

a = {1, 2, 3, 5, 7, 8, 9, 0}
b = {0, 2, 3, 4, 7, 8}


print(type(a))
#c = a & b
#d = a | b
#print(c)
#print(d)

a.intersection(b)
print(a)
a.union(b)
print(a)

a.add(2300)
print(a)
a.discard(2500)
# remove() will throw an error if element to be removed isn't present in the set. Hence, it's used inside if else
if 2500 in a:
    a.remove(2500)
else:
    print(f"Not present {2500}")

c = a.copy()
print(f"c has copy of sert a : {c}")
a.clear()
print(f"a after clearing {a}")
a = c.copy()
a.pop()
print(a)

a.pop()
print(a)
