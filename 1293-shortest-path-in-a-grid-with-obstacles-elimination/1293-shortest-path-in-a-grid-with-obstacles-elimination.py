class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        Q = deque([(0, 0, k, 0)]) # (r, c, k, steps)
        
        # if we have sufficient quotas to eliminate the obstacles in the worst case,
        # then the shortest distance is the Manhattan distance
        # if k >= ROWS + COLS - 2:
        #     return ROWS + COLS - 2
        
        visited = set()
        visited.add((0, 0, k)) # (r, c, remaining_obstacles)
        while Q:
            r, c, k, steps = Q.popleft()
            
            if (r, c) == (ROWS - 1, COLS - 1):
                return steps
            
            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS:
                    new_k = k - grid[row][col]
                    if new_k >= 0 and (row, col, new_k) not in visited:
                        visited.add((row, col, new_k))
                        Q.append((row, col, new_k, steps + 1))
        return -1
    