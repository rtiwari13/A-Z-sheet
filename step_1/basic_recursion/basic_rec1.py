# Print Numbers 

def print_no(n):

    # base case
    if n==0:
        return
    
    # tail recursion n to 1
    # print(n)
    # print_no(n-1)

    
    # head recursion 1 to n
    print_no(n-1)
    print(n)

print_no(5)