class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False
        
        # Determine if the first row, col needs to be 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        
        # Populate elements with 0s
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Check first col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # Check first row
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
        