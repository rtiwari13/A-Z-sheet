# Given an array of size N. Find the highest and lowest frequency element
# Input: arr = [1, 2, 2, 3, 3, 3]
# Output: 3

def find_highest_lowest_freq(nums):
    hl_dict = {}

    for i in nums:
        if i in hl_dict:
            hl_dict[i] += 1
        else:
            hl_dict[i] = 1

    result = []

  