class Solution:
    def digitCounts(self, n: int) -> int:
        # Write your solution here
        count = 0
        while n > 0:
            
            count += 1
            n//=10
        return count    
        pass