'''
Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0'''


def count_evens(nums):
  evens = []
  for num in nums:
    if num%2 ==0:
      evens.append(num)
  return len(evens)

print(count_evens([2,3,4,6,78,90,0]))