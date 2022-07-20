class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1. Initialize a Queue for BFS, total count of oranges, total minutes, and visited set.
        2. Iterate throught the matrix and add rotten oranges to the Queue and visited set
            and count total oranges.
        3. Perform BFS from the rotten oranges and maintain total minutes
        
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        Q = []
        oranges = minutes = 0
        visited = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    if grid[row][col] == 2:
                        Q.append((row, col))
                        visited.add((row, col))
                    oranges += 1
        
        # Peform BFS
        while Q:
            
            temp = []
            
            for r, c in Q:
                for (row, col) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col] == 1:
                        temp.append((row, col))
                        visited.add((row, col))
            
            minutes += 1 if temp else 0
            Q = temp
        
        return minutes if len(visited) == oranges else -1