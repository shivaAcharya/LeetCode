class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    target = matrix[i][j]
                    row, col = i, j
                    while row < ROWS and col < COLS:
                        if matrix[row][col] != target:
                            return False
                        row += 1
                        col += 1
        
        return True
