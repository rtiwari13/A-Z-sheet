# Print Numbers from 1 to N

def print_no(n):

    # base case
    if n==0:
        return
    
    # tail recursion
    print(n)
    print_no(n-1)

    # print("currently n is : ",n)
    
    # head recursion
    # print_no(n-1)
    # print(n)

print_no(5)