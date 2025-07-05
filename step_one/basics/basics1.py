# User Input / Output
# Complete the function printNumber which takes an integer input from the user and prints it on the screen.
# example : Input(user gives value): 7

Output: 7
class Solution:
    def printNumber(self):
        print("enter a number")
        user_input = int(input())
        print(user_input) 

sol = Solution()
sol.printNumber()
