class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ##### DIJKSTRA'S ALGORITHM ###############
        ROWS, COLS = len(heights), len(heights[0])
        
        heap = [(0, 0, 0)] # effort, row, col
        visited = set()
        
        while heap:
            
            effort, r, c = heapq.heappop(heap)
            
            if (r, c) in visited:
                continue
                
            if (r, c) == (ROWS - 1, COLS - 1):
                return effort
            
            visited.add((r, c))
            
            # Explore neighbors
            for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited:
                    max_effort = max(effort, abs(heights[r][c] - heights[row][col]))
                    heapq.heappush(heap, (max_effort, row, col))