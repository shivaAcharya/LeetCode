"""
https://leetcode.com/problems/out-of-boundary-paths/discuss/1293697/Python%3A-Easy-to-Understand-Explanation%3A-Recursion-and-Memoization-with-time-and-space-complexity.
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10**9 + 7

        # Initialize 3D DP array
        dp = [[[-1] * (maxMove + 1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            
            if maxMove < 0:
                return 0
            
            if i < 0 or i >= m or j < 0 or j >=n:
                return 1
            
            # Return if current value is already computed
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
            # Store in dp array after calculation
            dp[i][j][maxMove] = solve(i-1, j, maxMove - 1) + solve(i+1, j, maxMove - 1) + \
                                solve(i, j-1, maxMove - 1) + solve(i, j+1, maxMove - 1)
            
            return dp[i][j][maxMove]
        
        return solve(startRow, startColumn, maxMove) % M