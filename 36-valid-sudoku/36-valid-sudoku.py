class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        # Check ROWS

        for i in range(N):
            row = []
            for j in range(N):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])


          # Check COLS
        for i in range(N):
            col = []
            for j in range(N):
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.append(board[j][i])


          # Check Sub-Boards

        for r in range(0, N, 3):
            for c in range(0, N, 3):
                sub_board = []
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] != '.':
                            if board[r + i][c + j] in sub_board:
                                return False
                            sub_board.append(board[r + i][c + j])
        return True