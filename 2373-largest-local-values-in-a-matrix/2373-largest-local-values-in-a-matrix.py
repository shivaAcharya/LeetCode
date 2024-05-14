class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        res = [[1] * (N - 2) for _ in range(N - 2)]
        print(res)
        
        for r in range(1, N - 1):
            for c in range(1, N - 1):
                res[r - 1][c - 1] = max([grid[row][col] for row in (r - 1, r, r + 1) for col in (c - 1, c, c + 1)])
        
        return res
