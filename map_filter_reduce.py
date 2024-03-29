from functools import reduce

# MAP, FILTER, REDUCE

shop_items = [
    ("Product 1", 50),
    ("Product 2", 13),
    ("Product 3", 5),
]

print(type(shop_items))
print(shop_items[0])  # Should print first list element
print(shop_items[1])

items_gt_10 = list(filter(lambda item: item[1] >= 10, shop_items))
# here item iterates over each shop_item element, hence item[1] means we're filter cost
print(items_gt_10)

# MAP

y = map(lambda item: item[1], shop_items)
print(y)

# map() returns a map obj which is iterable. Hence, we iterate over it using for loop
for item in y:
    print(item)

# Or, we could use list() to get a list obj from map obj.

y_to_list = list(map(lambda item: item[1], shop_items))

### MAP | FILTER | REDUCE

nums = [0, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x != 0 and x % 2 == 0, nums))
odds = list(map(lambda a: a + 1, evens))
sum_odds = reduce(lambda m, n: m + n, odds)

print(f"numbers : {nums} and \nevens : {evens}\nodds : {odds}\nsum : {sum_odds}")

