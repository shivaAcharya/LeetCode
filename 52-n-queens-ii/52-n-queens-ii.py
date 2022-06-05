class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        cols, diags, anti_diags = set(), set(), set()
        
        def backtrack(row):
            if row == n:
                self.res += 1
                return 
            
            for col in range(n):
                # Find diag and anti_diag for this col
                diag, anti_diag = row - col, row + col
                
                # Check if current col is valid
                if col not in cols and diag not in diags and anti_diag not in anti_diags:
                    # Place the Queen
                    cols.add(col)
                    diags.add(diag)
                    anti_diags.add(anti_diag)
                    
                    # Explore new row
                    backtrack(row + 1)
                    
                    # Backtrack
                    cols.remove(col)
                    diags.remove(diag)
                    anti_diags.remove(anti_diag)
        
        backtrack(0)
        return self.res