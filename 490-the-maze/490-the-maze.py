class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Trivial case
        if start == destination:
            return True
        
        ROWS, COLS = len(maze), len(maze[0])
        
        visited = set()
        Q = deque([(start[0], start[1])])
        visited.add((start[0], start[1]))
        
        while Q:
            row, col = Q.popleft()
            
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = row + x, col + y
                
                while 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] == 0:
                    r += x
                    c += y
                    
                if [r - x, c - y] == destination:
                    return True
                
                if (r - x, c - y) not in visited:
                    visited.add((r - x, c - y))
                    Q.append((r - x, c - y))
        
        return False
                