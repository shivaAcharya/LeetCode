class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1:
            if n in seen: return False
            
            seen.add(n)
            cur = 0
            for digit in str(n):
                cur += (int(digit) ** 2)
            n = cur
        
        return True
            