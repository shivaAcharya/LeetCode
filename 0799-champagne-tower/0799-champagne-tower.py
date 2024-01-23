"""
Simulation

Initialize an array of arrays imitating the glass structure.
Initialize top glass with poured
Iterate through glasses.
    For each glass, calculate the flow
    q = x - 1
    left_bottom = r + 1, c
    right_bottom = r + 1, c + 1
    left and right bottom glasses get half of q wine
Return the amount of wine at query_row and query_glass

"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        arr = [[0] * n for n in range(1, query_row + 3)]
        arr[0][0] = poured
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (arr[r][c] - 1) / 2
                if q > 0:
                    arr[r + 1][c] += q
                    arr[r + 1][c + 1] += q
        
        return min(1, arr[query_row][query_glass])
        