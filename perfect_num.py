def isPerfectNumber(n):
    # Write your code here
    sqr = int(n**0.5)
    perfect = 1
    for i in range(2,sqr+1):
        if n % i == 0:
            perfect += i
            perfect = (n//i)+ perfect
    return perfect == n        
    pass

    