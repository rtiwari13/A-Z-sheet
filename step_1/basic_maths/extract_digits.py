# given a number n extract all the digits from it

def extract_digits(number):
    n = number 
    while n>0:  
        last_digit = n % 10
        print(last_digit)
        n = n//10   # Integer division to remove the last digit
        
extract_digits(883)