class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]
        
        # Fill last column and row in 1 as there is only one unique path from these cells
        for i in range(n):
            dp[m-1][i] = 1
            
        for i in range(m):
            dp[i][n-1] = 1
            
        # Populate all other cells from finish cell
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Skip last column and row
                if i != m - 1 and j != n - 1:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        return dp[0][0]