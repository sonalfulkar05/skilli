def isPalindrome(n):
    # Write your code here
    rev = 0
    a = n
    while n > 0:
        temp = n % 10
        rev = rev * 10 + temp
        n //= 10
    if rev == a:
        return True
    else:
        return False        
    pass