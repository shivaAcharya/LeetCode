class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        sub_islands = 0
        seen = set()
        is_subisland = True
        
        def dfs(r, c):
            nonlocal is_subisland
            if grid1[r][c] == 0:
                is_subisland =  False
            
            seen.add((r, c))
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen and grid2[nr][nc] == 1:
                    dfs(nr, nc)
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid2[row][col] == 1 and (row, col) not in seen:
                    dfs(row, col)
                    if is_subisland:
                        sub_islands += 1
                    is_subisland = True

        return sub_islands
        