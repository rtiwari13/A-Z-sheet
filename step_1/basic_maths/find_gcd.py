# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

# Examples:
# Input: n1 = 4, n2 = 6
# Output: 2


# Greatest Common divisor = 2.
# Input: n1 = 9, n2 = 8
# Output: 1

class GCD:

    def find_gcd (self, a, b):
        print("enter two numbers to find thier GCD")
        a = int(input("enter first:"))
        b = int(input("enter second:"))

        if a ==0 and b == 0:
            print("GCD is undefined")
            return None
        
        gcd =1

        for i in range (1,min(a,b)+1):
            if a%i==0 and b%i ==0:
                gcd = i
                
        print(gcd)
        return gcd
    
obj = GCD()
obj.find_gcd(0,0)