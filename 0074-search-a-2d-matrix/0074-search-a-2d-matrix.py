"""

[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

left = 0
right = m*n - 1 = 11 => 5

mid = 5

row = (mid) // COL => 1
col = (mid) % COL => 1

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW, COL = len(matrix), len(matrix[0])
        left, right = 0, ROW * COL - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // COL, mid % COL
            
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        