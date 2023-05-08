class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0
        N = len(mat)
        
        # primary diagonal
        for i in range(N):
            diag_sum += mat[i][i]
            
        # secondary diagonal
        for i in range(N):
            diag_sum += mat[i][N - i - 1]
        
        if N % 2:
            diag_sum -= mat[N // 2][N // 2]
        
        return diag_sum