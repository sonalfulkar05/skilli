def sumOfFrequencies(arr):
    # Write your code here
    frq={}
    for i in arr:
        frq[i]=frq.get(i,0)+1
    counts = sorted(set(frq.values()))
    large = counts[-1]  
    small = counts[0]
    return large + small  
    pass