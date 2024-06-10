class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == 0:
                return 1
            
            if i < 0:
                return 0
            
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        
        return dp(n)
    