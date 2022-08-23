class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        ROWS, COLS = len(maze), len(maze[0])
        
        dist = [[float("inf")] * COLS for _ in range(ROWS)]
        dist[start[0]][start[1]] = 0
        Q = deque([(start[0], start[1])])
        
        while Q:
            row, col = Q.popleft()
            
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = row + x, col + y
                count = 0
                while 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] == 0:
                    r += x
                    c += y
                    count += 1

                r -= x
                c -= y
                
                if dist[row][col] + count < dist[r][c]:
                    Q.append((r, c))
                    dist[r][c] = dist[row][col] + count
        
        ret = dist[destination[0]][destination[1]]
        
        return ret if ret != float("inf") else -1
                    
