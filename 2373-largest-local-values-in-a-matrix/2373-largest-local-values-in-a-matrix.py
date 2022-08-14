class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
              
        res = [[0] * (N - 2) for _ in range(N- 2)]
        
        for r in range(N-2):
            for c in range(N-2):
                for rr in range(r, r+3):
                    for cc in range(c, c+3):
                        res[r][c] = max(res[r][c], grid[rr][cc])
        
        return res