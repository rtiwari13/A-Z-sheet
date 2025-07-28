# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
#  The elements in the union must be in ascending order.

# The union of two arrays is an array where all values are distinct 
# and are present in either the first array, the second array, or both.

# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
# Output: [1, 2, 3, 4, 5, 7]

# Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
# Output: [1, 3, 4, 5, 6, 7, 8, 9]

def union_of_arrays(nums1,nums2):
    result = sorted(nums1+nums2)
    n = len(result)-1
    i=0
    while i<n:   
        if result[i] == result[i+1]:
            result.pop(i+1)
            n -=1
        else:
            i+=1
    return result

print(union_of_arrays([1, 2, 3, 4, 5],[1, 2, 7]))


# pythonic code
# def union_of_arrays(nums1, nums2):
#     return sorted(set(nums1 + nums2))
