def factorial(n):
    # Write your code here
    fact = 1
    for i in range(1,n+1):
        if i == 0:
            return 1

        fact*=i 
    return fact    
    pass