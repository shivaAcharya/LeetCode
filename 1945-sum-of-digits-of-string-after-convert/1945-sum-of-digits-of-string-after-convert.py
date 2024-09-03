class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        transform = ""
        
        for c in s:
            transform += (str(ord(c) - ord('a') + 1))
        
        while k:
            res = 0
            for digit in transform:
                res += int(digit)
            transform = str(res)
            # print(transform)
            k -= 1
        
        return res
        