def highestOccurringElement(nums):
    # Write your code here
    large=0
    ele = nums[0]
    for i in nums:
        count = nums.count(i)
        if count>large or (count == large and i <ele):
            large = count
            ele = i
    return ele        
    pass