test_string_01 = " Hello, world"
test_string_02 = "abc123"
print(f"LETTER 'o' APPEARS: {test_string_02.count('o')}\n")
print(f"IS LETTERS AND ALPHABETIC CHARS:  {test_string_02.isalpha()}")
print(f"IS DIGIT:  {test_string_02.isdigit()}")
print(f"IS LETTER and/or NUMBERS:  {test_string_02.isalnum()}")
print(f"IS NUMBERS:  {test_string_02.isnumeric()}")
sentence = "apple banana carrot"
list_fruits = sentence.split()
print(f"LIST  {list_fruits}")
joined = ",".join(list_fruits)
print(f"JOINED  {joined}")


