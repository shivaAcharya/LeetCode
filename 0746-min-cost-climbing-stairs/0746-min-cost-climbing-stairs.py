class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            step_one_cost = dp[i - 1] + cost[i - 1]
            step_two_cost = dp[i - 2] + cost[i - 2]
            dp[i] = min(step_one_cost, step_two_cost)
        
        return dp[-1]
    