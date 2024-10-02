class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            board[r][c] = 'T'
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                    capture(nr, nc)            
            
        
        # 1. (DFS) Capture unsorrounded region to T
        for r in range(ROWS):
            for c in range(COLS):
                if (r in (0, ROWS - 1) or c in (0, COLS - 1)) and board[r][c] == 'O':
                    capture(r, c)
        
        
        # 2. Capture all Os to Xs
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # Convert Ts to Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        