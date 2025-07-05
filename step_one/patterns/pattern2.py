
# Problem Statement: Given an integer N, print the following pattern : 
# Here, N = 5.
# Examples:
# Input Format: N = 3
# Result: 
# * 
# * * 
# * * *

# Input Format: N = 6
# Result:
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * * * *

# pattern 2

print("enter a number")
n = int(input(""))

for i in range(n):
    
    for j in range(i+1):
        print("*", end=" ")

    print()
