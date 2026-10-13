def findLcm(n1, n2):
    # Write your code here
    i = max(n1,n2)
    lcm = 1
    while True:
        if i % n1 == 0 and i % n2 == 0:
            lcm = i
            return lcm
            break
        i+=1 
    pass