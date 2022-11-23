class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Validate rows
        for i in range(9):
            rows = []
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in rows:
                        return False
                    rows.append(board[i][j])
        
        # Validate cols
        for i in range(9):
            cols = []
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in cols:
                        return False
                    cols.append(board[j][i])
        
        # Validate sub-box
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sub_box = []
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j].isdigit():
                            if board[r+i][c+j] in sub_box:
                                return False
                            sub_box.append(board[r+i][c+j])
        
        return True