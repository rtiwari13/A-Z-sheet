# Largest Element in an Array

# Given an array of integers nums, return the value of the largest element in the array
# Example: nums = [3, 3, 6, 1]
# Output: 6

# Input: nums = [3, 3, 0, 99, -40]
# Output: 99

def largest_element(nums):
    
    max = nums[0]
    for i in nums:       
        if i > max:
            max = i       
    return max

nums = [3, 3, 0, 99, -40]
print(largest_element(nums))