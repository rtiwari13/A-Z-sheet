# Pattern-5: Inverted Right Pyramid
# Examples:

# Input Format: N = 3
# Result: 
# * * *
# * * 
# *

# Input Format: N = 6
# Result:
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

print("enter a number")
n = int(input(""))

for i in range(n):
    
    for j in range(n-i):
        print("*", end=" ")
        

    print()
