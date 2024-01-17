class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Simulation
        1. Flow-through calculation on each glass.
        2. Initialize an array of arrays with proper number of glasses. Also, initialize topmost glass
        3. Iterate over each row and col.
        4.     left and right will have this flow q = (X - 1.0) / 2
        5.     (r + 1, c) and (r + 1, c + 1)
        
        """
        
        A = [[0] * r for r in range(1, query_row + 3)]
        A[0][0] = poured
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (A[r][c] - 1.0) / 2
                
                if q > 0:
                    A[r + 1][c] += q
                    A[r + 1][c + 1] += q
        
        return min(1, A[query_row][query_glass])
        