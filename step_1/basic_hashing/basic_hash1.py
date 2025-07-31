# Given an array:  
# we have found the number of occurrences of each element in the array
# example : nums = [1, 2, 2, 1, 3]
# Output: [[1, 2], [2, 2], [3, 1]]

# algo ->

# we got nums 
# take an empty dictionary  ( also called a hash map)  ==  key-value pair storage.
# iterate through each number in nums and count it like 
    #  If already in dictionary, increment count
    # if not then count it 1


def count_occurences(nums):
    occur_dict = {}

    for i in nums:
        if i in occur_dict:
            occur_dict[i] += 1
        else:
            occur_dict[i] = 1

    result = []

    for key , value in occur_dict.items():
        result.append([key,value])

    print(result)

    for key in sorted(occur_dict):
        print(f"{key} occurs {occur_dict[key]} times")

    return result

nums = [1 , 1 , 3, 8,8,9,5,3,6,7,1]
count_occurences(nums)