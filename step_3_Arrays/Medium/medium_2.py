# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
#  The sorting must be done in-place, without making a copy of the original array.

# Examples:
# Input: nums = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]

# Input: nums = [0, 0, 1, 1, 1]
# Output: [0, 0, 1, 1, 1]

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums)-1

    while mid<=high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            mid=mid+1
            low=low+1

        elif nums[mid] == 1:
            mid = mid +1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high = high-1

    return nums

print(sort_colors([1,2, 0, 2, 1, 0]))


