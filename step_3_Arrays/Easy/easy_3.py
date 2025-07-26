# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

# Input : nums = [1, 2, 3, 4, 5]
# Output : true


# Input : nums = [1, 2, 1, 4, 5]
# Output : false

def if_array_sorted(nums):
    n = len(nums)-1
    for i in range(n):        
            if nums[i] > nums[i+1]:
                return False
    return True

print(if_array_sorted([-1, 2, 3, 4, 5]))