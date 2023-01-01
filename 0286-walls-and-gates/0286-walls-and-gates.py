class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        
        Q = deque()
        
        # Initialize Q with gates
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    Q.append((r, c))
        
        level = 1
        Q.append((-1, -1))
        # BFS from all gates
        while Q:
            
            row, col = Q.popleft()
            if (row, col) == (-1, -1):
                level += 1
                if Q:
                    Q.append((-1, -1))
                continue
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= r < ROWS and 0 <= c < COLS and rooms[r][c] == 2147483647:
                    rooms[r][c] = level
                    Q.append((r, c))
                    