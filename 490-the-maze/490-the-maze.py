class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        ROWS, COLS = len(maze), len(maze[0])
        
        visited = set()
        
        def dfs(row, col):
            if (row, col) in visited:
                return False
            
            if [row, col] == destination:
                return True
            
            visited.add((row, col))
            
            r, l, u, d = col + 1, col - 1, row - 1, row + 1
            
            # Go right-most end
            while r < COLS and maze[row][r] == 0:
                r += 1
                
            if dfs(row, r-1): return True
            
            # Go left-most end
            while l >= 0 and maze[row][l] == 0:
                l -= 1
                
            if dfs(row, l+1): return True
                        
            # Go up-most end
            while u >= 0 and maze[u][col] == 0:
                u -= 1
            
            if dfs(u + 1, col): return True
            
            # Go down-most end
            while d < ROWS and maze[d][col] == 0:
                d += 1
                
            if dfs(d - 1, col): return True
            
                                         
            return False
                    

        return dfs(start[0], start[1])