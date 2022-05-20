class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        cache = [[0] * COL for _ in range(ROW)]
        
        # Get neighbors
        def get_neighbors(row, col):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            neighbors = []
            cur_elem = matrix[row][col]
            
            for r, c in directions:
                x, y = r + row, c + col
                
                # Check if possible_neigh is valid
                if 0 <= x < ROW and 0 <= y < COL and matrix[x][y] > cur_elem:
                    neighbors.append((x, y))
            
            return neighbors
        
        def dfs(m, n):
            # If visited return
            if cache[m][n] != 0:
                return cache[m][n]
            
            for x, y in get_neighbors(m, n):
                cache[m][n] = max(cache[m][n], dfs(x, y))
            
            cache[m][n] += 1
            return cache[m][n]
        
        ans = 0
        for i in range(ROW):
            for j in range(COL):
                ans = max(ans, dfs(i, j))
        
        return ans