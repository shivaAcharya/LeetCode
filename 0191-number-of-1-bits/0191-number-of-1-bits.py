class Solution:
    def hammingWeight(self, n: int) -> int:
        
        one_count = 0
        
        while n:
            if n % 2:
                one_count += 1
            n //= 2
        
        return one_count
    