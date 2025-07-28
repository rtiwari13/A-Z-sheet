# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), 
# return the only number missing from the array within this range.

# Examples:
# Input: nums = [0, 2, 3, 1, 4]
# Output: 5

# Input: nums = c
# Output: 3

def missing_number_in_range(nums):
    nums = sorted(nums)
    i=0
  
    while i<=len(nums)-1:
        if i == nums[i]:
            i +=1
        else:
            return i
    return i

print(missing_number_in_range([0, 2, 3, 1, 4]))

# pythonic code 
# def missing_number_in_range(nums):
#     n = len(nums)
#     return n * (n + 1) // 2 - sum(nums)
