def countPrimes(n):
    # Write your code here
    count = 0
    for i in range(2,n):
        isprime=True
        sqr = int(i**0.5)
        for j in range(2,sqr+1):
            if i % j == 0:
                isprime=False
        if isprime == True: 
            count += 1       
    return count        
    