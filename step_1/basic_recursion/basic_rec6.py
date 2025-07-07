# Given a string s, return true if the string is palindrome, otherwise false.


def check_palindrome(s, start , end):
    if start >= end:
        return True
    
    if s[start] != s[end] :
        return False
    
    return check_palindrome(s,start+1,end-1)

s = "aabbaaa"
result = check_palindrome(s,0,len(s)-1)
print(result)



def is_palindrome(s):
    if len(s) <=1:
        return True
    
    # If first and last characters are not equal ==  not palindrome
    if s[0] != s[-1]:
        return False
    
    # This slice removes the first and last characters from the string
    return is_palindrome(s[1:-1])
    

print(is_palindrome("hannah"))
print(is_palindrome("madam"))