"""
Perform Simulation

Initialize a 2D array immitating glasses
Top glass should have poured wine flow
For every left over, half should flow on the left bottom and the other half to the right bottom

"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        arr = [[0] * n for n in range(1, query_row + 3)]
        arr[0][0] = poured
        
        for r in range(query_row + 1):
            for c in range(len(arr[r])):
                q = (arr[r][c] - 1.0) / 2
                
                if q > 0:
                    arr[r + 1][c] += q
                    arr[r + 1][c + 1] += q
                    
        return min(1, arr[query_row][query_glass])
        