class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        if not num:
            return steps    
        
        for bit in bin(num)[2:]:
            if bit == '1':
                steps += 2
            else:
                steps += 1
        
        return steps - 1