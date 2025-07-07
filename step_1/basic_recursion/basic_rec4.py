# Given an array arr of n elements. The task is to reverse the given array.
#  The reversal of array should be inplace

def reverse_array(arr, start , end):
    if start >= end :
        return 
    
    # Pythonic swap - It swaps two elements in a single line —
    #  no need for a temporary variable.
    arr[start] , arr[end] = arr[end] , arr[start]

    reverse_array(arr  ,  start+1 ,  end-1 )
    


arr = [1,2,3,4,5,6]
reverse_array(arr,0,len(arr)-1)
print(arr)


