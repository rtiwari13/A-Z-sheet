# Given an array of integers nums and an integer target. 
# Return the indices(0 - indexed) of two elements in nums such that they add up to target.

# Input: nums = [1, 6, 2, 10, 3], target = 7
# Output: [0, 1]

# Input: nums = [1, 3, 5, -7, 6, -3], target = 0
# Output: [1, 5]

def two_sum(nums , target):
    output=[]
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
    return output

print(two_sum([1, 3, 5, -7, 6, -3],0))
