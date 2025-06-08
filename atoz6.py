# Pattern - 3: Right-Angled Number Pyramid
# Examples:

# Input Format: N = 3
# Result: 
# 1
# 1 2 
# 1 2 3

# Input Format: N = 6
# Result:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


print("enter a number")
n = int(input(""))

for i in range(n):
    
    for j in range(i+1):
        print(j+1, end=" ")

    print()
