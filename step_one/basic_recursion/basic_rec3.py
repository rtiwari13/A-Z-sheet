# Factorial

def print_factorial(n):
    if n == 1:
        return 1
    
    factorial = n * (print_factorial(n-1))
    return factorial


result = print_factorial(12)
print(result)