class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        cols, diagonals, anti_diagonals = set(), set(), set()
        
        def backtrack(row):
            # If found result, add to res and return
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            # Iterate over list of candidates (columns)
            for col in range(n):
                # Calculate diagonal and anit_diagonal value
                diag, anti_diag = row - col, row + col
                
                # If current column in valid
                if col not in cols and diag not in diagonals and anti_diag not in anti_diagonals:
                    # Place Queen
                    board[row][col] = 'Q'
                    
                    # Update sets
                    cols.add(col)
                    diagonals.add(diag)
                    anti_diagonals.add(anti_diag)
                    
                    # Call backtrack for new row
                    backtrack(row + 1)
                    
                    # Backtrack
                    board[row][col] = "."
                    cols.remove(col)
                    diagonals.remove(diag)
                    anti_diagonals.remove(anti_diag)
        
        backtrack(0)
        return res