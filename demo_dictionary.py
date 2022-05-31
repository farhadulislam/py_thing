import pprint

dict1 = {'name': 'Toyota', 'model': '1996', 'colour': 'White'}
dict2 = {'name': 'Audi', 'model': '2012', 'colour': 'Blue'}


#Dictionary is unoirdered however, from 3.7 and avobe dictionary remembers insertion order of element.
#However, this shouldn't be relied upon.

list1_from_dict1 = list(dict1)

print(list1_from_dict1)

print(dict1['name'])

for k in dict1.keys():
    print('dict1 keys :'+ k)
for v in dict1.values():
        print('dict1 values :' + v)
for i in dict1.items():
    print(i)

#inserting key, values into dict

dict1['mileage']='100000 miles'

print(dict1)

print("DICTIONARY WITH MIX VALUES")

dict3 = {
    'name': 'BMW',
    'colour': 'Red',
    'model': '2015',
    'mileage': 65000,
    'brand_new': False
}

print('Priting dict2')
print(str(type(dict3))+ str(len(dict3)))
pprint.pprint(dict3)
