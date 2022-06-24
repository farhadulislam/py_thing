#TUPLE DEMO
#TUPLE allows duplicates
#TUPLE is unodered
#TUPLE items can be of any types

tuple_1 = ('Chittagong', 'Dhaka', 'Munshiganj', 'Sirajganj', 'Comilla', 'Feni', 'Lalmonirhat')

print(tuple_1)

#INSERT into a tuple. Convert tuple into list, appned an item, and then finally revert it to tuple
#This is beacuse tuple is IMMUTABLE

list1_from_tuple_1 = list(tuple_1)
list1_from_tuple_1.append('Rajshahi')
print(list1_from_tuple_1)
tuple_1 = tuple(list1_from_tuple_1)
print(tuple_1)

#ONE ITEM TUPLE, ensure a comma is placed
tuple_2 =('One',)
print(type(tuple_2))

# Below isn't a TUPLE
tuple_3 =('One')
print(type(tuple_3))


composite_tuple = ('String', [12, 34, 5], True, 'Fruits')
print(composite_tuple)
print(composite_tuple[1][2])
print(composite_tuple.count('String'))