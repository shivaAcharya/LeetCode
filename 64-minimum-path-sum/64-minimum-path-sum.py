class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dp = [[-1] * COLS for _ in grid]
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                
                # Fill last row
                if i == ROWS - 1 and j != COLS - 1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                    
                # Fill last col
                elif j == COLS - 1 and i != ROWS - 1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                
                # Everything except bottom right cell
                elif i != ROWS - 1 and j != COLS - 1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                
                # Fill bottom right cell same as grid
                else:
                    dp[i][j] = grid[i][j]
                                                
        return dp[0][0]
        
                