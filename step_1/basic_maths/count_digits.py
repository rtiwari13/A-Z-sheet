# Count all Digits of a Number
# You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.

# Examples:
# Input: n = 4
# Output: 1

# Explanation: There is only 1 digit in 4.

# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.

class Solution:
    def count_digits(self,n):
        print("Enter number to count digits")
        n = int(input())
        n = abs(n)
        if n==0:
            return 1
        count = 0
        while n > 0:
            n = n // 10 
            count = count +1
        print(count)
        return count

obj = Solution()
obj.count_digits(0)
