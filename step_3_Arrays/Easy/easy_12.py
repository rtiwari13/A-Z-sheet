# Given an array of nums of n integers. 
# Every integer in the array appears twice except one integer.
# Find the number that appeared once in the array.

# Examples:
# Input : nums = [1, 2, 2, 4, 3, 1, 4]
# Output : 3

# Input : nums = [5]
# Output : 5

# any number XOR with itself is 0
# a ^ 0 = a
# a ^ a = 0

def appeared_once(nums):
    count = 0
    for i in nums:     
            count ^= i
    return count
        
print(appeared_once([1, 2, 2, 4, 3, 1, 4]))