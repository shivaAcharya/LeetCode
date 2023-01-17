class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def to_int(s):
            res = 0
            for n in s:
                res = res * 10 + ord(n) - ord('0')
            
            return res
        
        def to_str(i):
            if not i: return '0'
            
            res = []
            while i:
                n = chr(i % 10 + ord('0'))
                res.append(n)
                i //= 10
            
            return "".join(reversed(res))
        
        res_int = to_int(num1) * to_int(num2)
        
        return to_str(res_int)
            