list0 = ['one', 'two', 'three', 'four', 'five']
list1 = [1, 2, 3, 4, 5, 50, 60, 70]
list2 = ['orange', 'mango', 'jackfruit', 'watermelon', 'grapes']

list_all = list(zip(list0, list1, list2))
print(list_all)
for i in list_all:
    print(list(i))


mishkat_tuple = (20, 30, 40, 50, 50, 50, 50, 50, 50)
miskat_set = set(mishkat_tuple)

print(f"Mishkat's tuple : {mishkat_tuple}")
print(f"Mishkat's set : {miskat_set}")
