# Given an integer array nums, move all the 0's to the end of the array. 
# The relative order of the other elements must remain the same.
# This must be done in place, without making a copy of the array.

# Examples:
# Input: nums = [0, 1, 4, 0, 5, 2]
# Output: [1, 4, 5, 2, 0, 0]

# Input: nums = [0, 0, 0, 1, 3, -2]
# Output: [1, 3, -2, 0, 0, 0]

def move_zeros_to_the_end(nums):
    
   non_zero_place = 0
   for i in range(len(nums)):
      if nums[i] != 0:
         nums[non_zero_place] = nums[i]
         non_zero_place += 1
   for i in range(non_zero_place, len(nums)):
      nums[i] = 0
   return nums
print(move_zeros_to_the_end([0, 1, 4, 0, 5, 2]))