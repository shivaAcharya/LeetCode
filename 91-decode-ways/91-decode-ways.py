class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            elif s[i] == '1' and i + 1 < len(s):
                dp[i] = dp[i+1] + dp[i+2]
                
            elif s[i] == '2':
                dp[i] = dp[i+1]
                
                if i + 1 < len(s) and s[i+1] <= '6':
                    dp[i] += dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]

    
"""
FAILED TESTCASES

1. "1"
2. "12"

"""