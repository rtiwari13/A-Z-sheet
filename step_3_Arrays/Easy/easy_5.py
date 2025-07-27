# Given an integer array nums, rotate the array to the left by one.

# Examples:
# Input: nums = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]

# Input: nums = [-1, 0, 3, 6]
# Output: [0, 3, 6, -1]

def rotate_array_left_by_one(nums):

    first = nums[0]
    nums.pop(0)
    nums.append(first)
    

    return nums

# pythonic solution
def rotate_array_by_one(nums):
    return nums[1:]+ nums[:1]

print(rotate_array_left_by_one([1, 2, 3, 4, 5]))
print (rotate_array_by_one([-1, 0, 3, 6]))