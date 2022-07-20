
sentence = "This is a sentence"
print('This is \'nt a joke')

title = "This IS A Title"
print(title.istitle())

age = str(36)
print(age.isdecimal)

print(sentence.istitle())

uni = 'university'
print(uni.upper())

uni_upper = uni.upper()
print(f"{uni_upper } is in uppercase : \t")
print(uni_upper.isupper())

uni_lower = uni_upper.lower()
print(f"{uni_lower} is lower : ")
print(uni_lower.islower())
print(uni_lower.islower())

alphanumeric = "ABCH123"
print(f"{alphanumeric} is alphanumric")
print(alphanumeric.isalpha())


hello_world = "Hello, world!"

print(hello_world.startswith("Hello"))
print(hello_world.startswith("World"))


print(' '.isspace())

#The join() method is called on a string, gets passed a list of strings, and returns a string.
