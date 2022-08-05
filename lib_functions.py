import math
list0 = [1, 23, 45, 67, 80, 90]

print(f"Sum of all items {sum(list0)}")
print(f"Min : {min(list0)}")
print(f"Max : {max(list0)}")
print(f"Absolute value : {abs(-1)}")
print(10//3)
print(f"divmod : {divmod(11,3)}")

number = 15
print(f"Binary of {number}", bin(number))
print(f"Oct of {number}", oct(number))
print(f"Hex of {number}", hex(number))
print(f"Binary of {number}", bin(number))

print(round(math.pi),2)

reversed_list0 = reversed(list0)
print(list(reversed_list0))

prog_lang = 'Python'
print("".join(reversed(prog_lang)))

#char to ascii, use ord() and chr() for chr to ascii
list_ascii = []
for item in ['a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3']:
    list_ascii.append(ord(item))
print(list_ascii)

list_chars = []
for item in list_ascii:
    list_chars.append(chr(item))
print(list_chars)

prog_lang = ['Java', 'Pyhton', 'Go', 'Julia']
i = 1
enm_prog_lang =[]
for item in prog_lang:
    enm_prog_lang.append([i, item])  # append() takes exactly 1 arg; hence, had to use each element as list
    i += 1
print(enm_prog_lang)

enm_prog_lang_2 = [x for x in enumerate(prog_lang, start = 1)]
print(enm_prog_lang_2)

print(list(map(int, ['0','12','23','99']))) # map() returns a map obj, so, used list()
squared = map(lambda x : pow(x, 2), [1,2,3])
print(list(squared))

java = prog_lang[0]
print(java[::-1])
print(java[-1])
print('madam'[::-1]=='madam') # check if it is palindrome
hundred_nums = list(range(1,101))
print(list(filter(lambda x: x%2==0 and x < 30, hundred_nums)))