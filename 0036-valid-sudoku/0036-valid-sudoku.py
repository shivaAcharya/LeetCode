"""
Clarifying questions:
1. Board will always be 9 x 9
2. Contains str version of num

Approach
1. Traverse each row and check if valid.
2. Traverse each column and check if valid.
3. Traverse each 3 x 3 sub-boxes and check if valid.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows
        for r in range(9):
            nums = []
            for c in range(9):
                element = board[r][c]
                if element.isnumeric() and element in nums:
                    return False
                nums.append(element)
        
        # Check cols
        for r in range(9):
            nums = []
            for c in range(9):
                element = board[c][r]
                if element.isnumeric() and element in nums:
                    return False
                nums.append(element)
        
        # Check 3 x 3
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = []
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        element = board[i][j]
                        if element.isnumeric() and element in nums:
                            return False
                        nums.append(element)
        
        return True
"""
RE:


"""