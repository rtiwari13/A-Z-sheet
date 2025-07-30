def move_zeros_to_the_end(nums):
    n = len(nums)-1
    high = len(nums)-1
    mid = 0
    
    for i in range(n):
        if nums[mid] == 0:
            nums[mid], nums[high] = nums[high],nums[mid]
            mid=mid+1
            high = high-1
        else:
           high = high-1
           mid = mid + 1 

    return nums

print(move_zeros_to_the_end([0, 1, 4, 0, 5, 2]))