class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_path_sum = float("inf")
        N = len(matrix)
        memo = {}
        def dfs(r, c):
            # Base cases
            if (r, c) in memo:
                return memo[(r, c)]
            
            if c < 0 or c == N:
                return float("inf")
            
            if r == N - 1:
                return matrix[r][c]
            
            cur_sum = []
            for row, col in (r + 1, c), (r + 1, c + 1), (r + 1, c - 1):
                cur_sum.append(dfs(row, col))

            memo[(r, c)] = min(cur_sum) + matrix[r][c]
            return memo[(r, c)]
        
        for col in range(N):
            min_path_sum = min(min_path_sum, dfs(0, col))
            
        return min_path_sum
        