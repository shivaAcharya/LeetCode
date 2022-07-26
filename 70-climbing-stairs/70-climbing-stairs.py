class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def recurse(step):
            if step > n:
                return 0
            
            if step == n:
                return 1
            
            if step in memo:
                return memo[step]
            
            memo[step] = recurse(step + 1) + recurse(step + 2)
            
            return memo[step]
        
        return recurse(0)
        