# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.

# Input : nums = [4, 2, 2, 6, 4], k = 6
# Output : 4

# Input :nums = [5, 6, 7, 8, 9], k = 5
# Output : 2


# brute force
def xor_equals_to_k(nums,k):

    number = 0

    for i in range (len(nums)):
        x_temp = 0
        for j in range(i,len(nums)):
            x_temp ^= nums[j]

            if x_temp == k:
                number += 1 
    return number

print(xor_equals_to_k([4, 2, 2, 6, 4],6))