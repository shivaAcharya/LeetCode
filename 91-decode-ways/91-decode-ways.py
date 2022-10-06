class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)
        dp = [0] * (N + 1)
        dp[-1] = 1
        
        for i in range(N - 1, -1, -1):
            
            if s[i] == '0':
                dp[i] = 0
            
            elif s[i] == '1':
                dp[i] += dp[i+1]
                if i + 1 < N:
                    dp[i] += dp[i+2]
            
            elif s[i] == '2':
                dp[i] += dp[i+1]
                if i + 1 < N and s[i+1] <= '6':
                    dp[i] += dp[i+2]
            
            else:
                dp[i] = dp[i+1]
        
        return dp[0]
        