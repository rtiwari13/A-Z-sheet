# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

def natural_numbers_sum(n):
    # base condition 
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    sum = n + natural_numbers_sum(n-1)
    return sum
    
result = natural_numbers_sum(999)
print(result)