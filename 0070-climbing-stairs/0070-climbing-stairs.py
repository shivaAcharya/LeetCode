class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        
#         memo = {}
        
#         def dfs(n, steps):
#             if n in memo:
#                 return memo[n]
#             if n < 0:
#                 return 0
#             if n == 0:
#                 return 1
            
#             memo[n] = dfs(n - 1, steps) + dfs(n - 2, steps)
#             return memo[n]
        
#         return dfs(n, 0)
        