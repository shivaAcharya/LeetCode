class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = COLS = 9

        # Check each row
        for r in range(ROWS):
            rows = set()
            for c in range(COLS):
                cur = board[r][c]
                if cur != "." and cur in rows:
                    return False
                rows.add(board[r][c])

        # Check each column
        for c in range(COLS):
            cols = set()
            for r in range(ROWS):
                cur = board[r][c]
                if cur != "." and cur in cols:
                    return False
                cols.add(board[r][c])

        # Check grid
        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                grid = set()
                for i in range(3):
                    for j in range(3):
                        cur = board[r + i][c + j]
                        if cur != "." and cur in grid:
                            return False
                        grid.add(board[r + i][c + j])

        return True