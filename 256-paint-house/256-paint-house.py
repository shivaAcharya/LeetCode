class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        
        def paint(n, color):
            if (n, color) in memo:
                return memo[(n, color)]
            total_cost = costs[n][color]
            
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint(n+1, 1), paint(n+1, 2))
            elif color == 1:
                total_cost += min(paint(n+1, 0), paint(n+1, 2))
            elif color == 2:
                total_cost += min(paint(n+1, 0), paint(n+1, 1))
            memo[(n, color)] = total_cost
            return total_cost
        
        return min(paint(0, 0), paint(0, 1), paint(0, 2))