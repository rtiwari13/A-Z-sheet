# Pattern - 4: Right-Angled Number Pyramid - II

# Here, N = 5.

# Examples:

# Input Format: N = 3
# Result: 
# 1
# 2 2 
# 3 3 3

# Input Format: N = 6
# Result:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

print("enter a number")
n = int(input(""))

for i in range(n):
    
    for j in range(i+1):
        print(i+1, end=" ")

    print()