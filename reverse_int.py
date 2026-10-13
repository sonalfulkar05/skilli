def reverseInteger(n):
    # Write your code here
    rev = 0 
    while n > 0:
        temp = n % 10
        rev = rev * 10 + temp
        n//=10
    return rev     
    pass