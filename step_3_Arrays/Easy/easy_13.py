# Given an array nums of size n and an integer k,
#  find the length of the longest sub-array that sums to k.
#  If no such sub-array exists, return 0.

# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
# Output: 4

# Input: nums = [-3, 2, 1], k=6
# Output: 0

# brute force : count sum of each sub array 

def longest_sub_array(nums,k):
    max_length = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i , len(nums)):
            sum += nums[j]
            
            if sum == k:
                max_length = max(max_length,j-i+1)
    
    return max_length 

print(longest_sub_array([10, 5, 2, 7, 1, 9],  15))