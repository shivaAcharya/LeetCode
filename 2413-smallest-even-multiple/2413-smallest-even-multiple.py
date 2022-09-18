class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n % 2:
            return n * 2
        
        return n if n != 1 else 2