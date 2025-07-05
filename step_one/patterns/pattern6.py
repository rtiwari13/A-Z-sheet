# Pattern - 6: Inverted Numbered Right Pyramid
# Examples:

# Input Format: N = 3
# Result: 
# 1 2 3
# 1 2
# 1

# 
# 
# Input Format: N = 6
# Result:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

print("enter a number")
n = int(input(""))

for i in range(n):
    
    for j in range(n-i):
        print(j+1, end=" ")
        

    print()

