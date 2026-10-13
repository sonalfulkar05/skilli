def countOddDigits(n):
    # Write your code here
    count = 0

    while n > 0:
        a= n%10
        if a % 2 != 0:
            count += 1
            n//=10
        else:
            n//=10
    
    return count        
    pass