# Given an integer array nums sorted in non-decreasing order, 
# remove all duplicates in-place so that each unique element appears only once.
# Return the number of unique elements in the array.

# Examples:
# Input: nums = [0, 0, 3, 3, 5, 6]

# Output: 4
# Explanation: Resulting array = [0, 3, 5, 6, _, _]
# There are 4 distinct elements in nums and the elements marked as _ can have any value.

# Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]
# Output: 4
# Explanation: Resulting array = [-2, 2, 4, 5, _, _, _, _]
# There are 4 distinct elements in nums and the elements marked as _ can have any value.

def remove_duplicates(nums):
    n=len(nums)-2 
    count = 0 

    for i in range(n): 
        if nums[i+1] == nums[i]:
            count = count+1
    return n-count+2
 
print(remove_duplicates([0, 0, 3, 3, 5, 6]))

