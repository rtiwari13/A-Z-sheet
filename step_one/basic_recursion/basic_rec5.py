# The Fibonacci numbers, commonly denoted F(n) form a sequence, 
#  called the Fibonacci sequence, such that
#  each number is the sum of the two preceding ones, 
#  starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

def fibonacci_number(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fibonacci_number(n-1) + fibonacci_number(n-2)

def print_fibonacci_series(n):
    print(f"Fibonacci series up to {n} terms:")
    if n <=0:
        return 0
    if n==1:
        return 1
    
    i,j = 0,1
    for _ in range (n):
        print(i, end=" ")
        i,j = j, i+j
        print()


print_fibonacci_series(17)

result = fibonacci_number(17)
print("fibonacci number:", result)

