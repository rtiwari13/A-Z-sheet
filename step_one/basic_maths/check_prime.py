# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.
# Examples:
# Input: n = 5
# Output: true
# Input: n = 8
# Output: false

class Solution:
    def check_prime(self, n):
        print("Enter a number to check if it is prime or not")
        n = int(input())

        # brute force

        # if n <=1:
        #     print(False)
        #     return False
        
        # for i in range (2,n):
        #     if n%i == 0:
        #        print(False)
        #        return False
        # print(True)
        # return True

        

obj = Solution()
obj.check_prime(0)