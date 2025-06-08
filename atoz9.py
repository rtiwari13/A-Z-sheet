# Pattern - 6: Inverted Numbered Right Pyramid
# Examples:

# Input Format: N = 3
# Result: 
# 1 2 3
# 1 2
# 1

# plan for this night to tomorrow's afternoon 
# - all night backend for ziplink 
# - 2 hour dsa (maintaining streak for dsa ) 
# - clustered list but (python,javascript, react , postgresSQL roadmaps from roadmap.sh)

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

