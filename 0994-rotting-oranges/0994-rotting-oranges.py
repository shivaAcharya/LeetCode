class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        Q = deque()
        fresh_oranges = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    Q.append((r, c))
                    
        minutes = 0
        
        while Q and fresh_oranges:
            minutes += 1
            for _ in range(len(Q)):
                r, c = Q.popleft()
                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        Q.append((nr, nc))
        
        return minutes if not fresh_oranges else -1
        