# Given an array of integers nums and an integer target, 
# find the smallest index (0 based indexing) where the target appears in the array. 
# If the target is not found in the array, return -1

# Examples:
# Input: nums = [2, 3, 4, 5, 3], target = 3
# Output: 1

# Input: nums = [2, -4, 4, 0, 10], target = 6
# Output: -1

def find_smallest_index(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:        
            return i

    return -1

print(find_smallest_index([2, 3, 4, 5, 3], 3))