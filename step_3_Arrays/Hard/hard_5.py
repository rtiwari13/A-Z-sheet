# You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.



# Return the length of such a subarray. If no such subarray exists, return 0.


# Examples:
# Input: arr = [15, -2, 2, -8, 1, 7, 10, 23]

# Output: 5

# Explanation:

# The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.

# Input: arr = [2, 10, 4]

# Output: 0

# Explanation:

# There is no subarray whose elements sum to 0.

def sum_equals_to_zero(nums):
    max_length = 0
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum +=nums[j]

            if sum == 0 :
                max_length = max(max_length,j-i+1)

    return max_length

print(sum_equals_to_zero([15, -2, 2, -8, 1, 7, 10, 23]))