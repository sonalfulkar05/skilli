def isArmstrong(n):
    # Write your code here
    a = n
    count = len(str(n))
    sums =0
    while n > 0:
        b = n % 10
        sums = sums + b**count
        n //=10
    if sums == a:
        return True
    else:
        return False        
    pass