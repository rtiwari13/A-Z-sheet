# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called it's divisor.

# Examples:
# Input: n = 6
# Output = [1, 2, 3, 6]

# Input: n = 8
# Output: [1, 2, 4, 8]

class Div:
    def find_divisor(self,n):
        print("Enter a number to find its divisior")
        n = int(input())
        divisor = []
        for i in range (1 , n+1):
            if n%i == 0:
                divisor.append(i)
        print(divisor)
        return divisor

div_obj = Div()
div_obj.find_divisor(0)