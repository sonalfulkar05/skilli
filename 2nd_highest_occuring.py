def secondHighestOccurringElement(arr):
    # Write your code here
    frq ={}
    for i in arr:
        frq[i] = frq.get(i,0)+1
    counts = sorted(set(frq.values()),reverse=True)
    s_large=counts[1]
    match_ele=[ ]
    for i in frq:
        if frq[i] == s_large:
            match_ele.append(i)
    return min(match_ele)            
    pass