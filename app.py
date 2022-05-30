#DEMO APP

print("Demo Python app")

print('ENTER YOUR NAME')
name = input()
if name =='':
    print('NAME MUST NOT BE EMPTY')

print('ENTER AGE')
#age = input()
age = int(input())


if not isinstance(age, (int, float)):
    pass
else:
    age = int(age)
    print('NAME: ' + name + ', AGE: ' + str(age))
    print('LENGTH : ' + str(len(name)))

print(name.strip().isdigit())
print(isinstance(age, (int, float)))

