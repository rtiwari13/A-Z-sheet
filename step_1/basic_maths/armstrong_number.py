def armstrong_number(N):
    original = N
    sum = 0
    while N > 0:
        last_digit = N% 10

        sum = sum + ((last_digit*last_digit*last_digit))

        N = N//10

    if sum == original :
        print(sum)
        print("yes")
    else:
        print(sum)
        print("no")

armstrong_number(371)