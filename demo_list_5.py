nums = [23, 45, 67, 89, 91, 33, 33, 0, 1, 55, 67, 89, 91]
print(nums)
nums.sort()
print(f"Sorterd nums : {nums}")
print(f"Min : {min(nums)}")
print(f"Max : {max(nums)}")
print(f"Sum : {sum(nums)}")
print(f"Count  : {nums.count(89)}")
nums.extend([200, 300, 400, 500])
print(nums)


for index,number in enumerate(nums):
    print(index,number)

matrix = [[0,1], [2,3]]
zeroes = [0] * 5
print(zeroes)
chars = list("Universal")
print(chars)

numbers = list(range(20))
print("Every other number")
print(numbers[::2])
#*other takes all other elements from the list
first, second, *other = numbers
print(f"first element {first},\nsecond element {second},\nothers {other}")

first, *other, last = numbers
print(f"first element {first},\nlast element {last},\nothers {other}")


####### A I P R D ############

letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

#add
letters.append('w')
print(letters)
letters.insert(0, 'k')
print(letters)

#remove
letters.pop()
print(letters)
letters.remove('k')
print(letters)
del letters[0:3]
print(letters)


print(letters.index('e'))






