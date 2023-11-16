class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m = 1, n = 1 => 0
        
        m = 2, n = 2
        
         | | |
         | | |
         
         m = 3, n = 2
         
         |  |  |
         |  |  |
         |  |  |
         
         m = 3, n = 7
         
         |  |  |  |  |  |  |  |
         |  |  |  |  |  |  |  |
         | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 
         
        """
        
        dp = [[1] * n for _ in range(m)]
        
        # print(dp)
        
        for r in range(m - 2, -1, -1): # [5, 0]
            for c in range(n - 2, -1, -1): #[1, 0]
                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]
        
        return dp[0][0]        
        