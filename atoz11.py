# Reverse a number
# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

# Examples:
# Input: n = 123
# Output: 321

class Solution:
    def reverse_number(self,n):
        print("Enter number to reverse")
        n = int(input())

        # handling negative numbers
        sign = -1 if n<0 else 1
        n = abs(n)

        reverse = 0

        while n>0:
            digit = n%10    # last digit of n
            reverse = reverse * 10 + digit
            n = n //10      # remove last digit

        print(sign*reverse)
        return sign*reverse
        

obj = Solution()
obj.reverse_number(0)
