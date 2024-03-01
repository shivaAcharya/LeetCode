class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        res = ['0'] * len(s)
        one_count = s.count('1')
        
        if one_count >= 1:
            res[-1] = '1'
            one_count -= 1
        i = 0
        while one_count:
            res[i] = '1'
            i += 1
            one_count -= 1
        
        return "".join(res)
    