from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache
        def dfs(n, steps):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            return dfs(n - 1, steps) + dfs(n - 2, steps)
        
        return dfs(n, 0)
    