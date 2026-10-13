def returnLargestDigit(n):
    # Write your code here
    m = 0
    while n > 0:
        b = n % 10
        if b > m:
            m = b
        n//=10
    return m    

    pass