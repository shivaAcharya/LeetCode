class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def recursion(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            cur_cost = cost[i] + min(recursion(i+1), recursion(i+2))
            memo[i] = cur_cost
            return cur_cost
    
        return min(recursion(0), recursion(1))
            
                