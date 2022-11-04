class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        
        def check(row, num):
            for n in mat[row]:
                if n == num:
                    return True
                if n > num:
                    return False
        
        for num in mat[0]:
            
            for r in range(1, ROWS):
                if not check(r, num):
                    break
                if r == ROWS - 1:
                    return num
        
        return -1