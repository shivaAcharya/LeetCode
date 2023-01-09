class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])
        start_color = image[sr][sc]
        flood_fill_image = deepcopy(image)
        
        # DFS
        def dfs(r, c):
            flood_fill_image[r][c] = color
            image[r][c] = -1 # mark visited
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == start_color:
                    dfs(nr, nc)
        
        dfs(sr, sc)
        return flood_fill_image