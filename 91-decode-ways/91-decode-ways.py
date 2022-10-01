class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        @cache
        def dfs(i):
            
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            if i == len(s) - 1:
                return 1
            
            res = dfs(i+1)
            
            if int(s[i : i + 2]) <= 26:
                res += dfs(i + 2)
            
            return res
        
        return dfs(0)

    
"""
FAILED TESTCASES

1. "1"
2. "12"

"""