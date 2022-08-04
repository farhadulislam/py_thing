def sum13(nums):
  sum = 0
  for i in nums:
    if i == 13:
      index_to_add_from = nums.index(i)+1
      while (index_to_add_from < len(nums)):
        if nums[index_to_add_from] == 13:
          index_to_add_from = index_to_add_from + 1
          sum += nums[index_to_add_from]
        else:
          sum += nums[index_to_add_from]
          index_to_add_from =  index_to_add_from + 1
    elif len(nums) ==0:
      return 0
    else:
      sum += i
  return sum