#a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

vegs = ['Onions', 'Garlic', 'Tomatoes', 'Cabbage', 'Cauliflower', 'Aubergine', 'Raddish', 'Beans']
#last two items reveresed.

years = [1990, 1998, 1989, 1995, 2010, 2011, 2015, 2016, 2022, 1952, 1971]

# start at 4th element (index 3) and go through rest of the list array.
print(vegs[3:])
# Start from beginning but stop before 4th element (index 3)
print(vegs[:3])

#last two items, the other way to understand this is look at negative indexing which points at second last element and
# then look at : syntax which says everything after second last hence, syntax is -2:
print(vegs[-2:])
#All items except last two
print(vegs[:-2])


# All items but reversed.
print(vegs[::-1])
#First two items reveresed.
print(vegs[1::-1])
#last two items reveresed.
print(vegs[:-3:-1])
#Everything except two reversed.
print(vegs[-3::-1])

