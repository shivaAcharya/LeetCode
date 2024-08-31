"""
Clarifying questions:
1. Board will always be 9 x 9
2. Contains str version of num

Approach
1. Traverse each row and check if valid.
2. Traverse each column and check if valid.
3. Traverse each 3 x 3 sub-boxes and check if valid.

"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element != '.':
                    if element in rows[r] or element in cols[c] or element in grids[(r // 3, c // 3)]:
                        return False
                    rows[r].add(element)
                    cols[c].add(element)
                    grids[(r // 3, c // 3)].add(element)
        return True
        
"""
RE:


"""