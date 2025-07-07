# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
# A palindrome number is a number which reads the same both left to right and right to left.

# Examples:
# Input: n = 121
# Output: true

# Input: n = 123
# Output: false

class Solution:
    def check_palindrome(self, n):
        print("Enter a number to check palindrome")
        n = int(input())

        original_number = n
        reverse = 0

        while n > 0:
            reverse = reverse*10+n%10
            n = n // 10

        is_palindrome = (original_number == reverse)
        print(is_palindrome)
        return is_palindrome

obj = Solution()
obj.check_palindrome(0)