def isPrime(n):
    # Write your code here
    sqr = int(n**00.5)
    if n < 2:
        return False

    for i in range(2,sqr+1):
        
        if n % i == 0:
            return False
    return True    
    pass