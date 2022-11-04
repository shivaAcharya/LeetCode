class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        '''
        1. Since the elements are stricty increasing => No duplicates
        2. Count the frequency of every element and return the first element with the frequency equal to the number of rows.
        
        '''
        ROWS, COLS = len(mat), len(mat[0])
        frequency = {}
        
        for c in range(COLS):
            for r in range(ROWS):
                num = mat[r][c]
                frequency[num] = frequency.get(num, 0) + 1
                if frequency[num] == ROWS:
                    return num
        return -1
        
        '''
        ################### SIMULATION APPROACH TIME COMPLEXITY => O(M^2N^2)
        
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
        '''