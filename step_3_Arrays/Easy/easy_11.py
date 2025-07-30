# Given a binary array nums,
# return the maximum number of consecutive 1s in the array.

# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
# Output: 3

# Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]
# Output: 0


def max_consecutive_ones(nums):
    current_count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count


print(max_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0]))
