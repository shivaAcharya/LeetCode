class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            
            memo[i] = cost[i] + min(dp(i + 1), dp(i + 2))
            return memo[i]
        
        return min(dp(0), dp(1))
            