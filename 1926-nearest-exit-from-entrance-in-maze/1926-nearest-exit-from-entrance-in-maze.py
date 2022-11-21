class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        entrance.append(0)
        Q = deque([entrance])
        maze[entrance[0]][entrance[1]] = '+'
        
        # BFS
        while Q:
            row, col, steps = Q.popleft()
            
            maze[row][col] = '+'
            
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] == ".":

                    Q.append((r, c, steps + 1))
                    maze[r][c] = '+'
                    
                    # Check for exit
                    if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                        return steps + 1
        
        return -1
#         rows, cols = len(maze), len(maze[0])
#         dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
#         # Mark the entrance as visited since its not a exit.
#         start_row, start_col = entrance
#         maze[start_row][start_col] = "+"
        
#         # Start BFS from the entrance, and use a queue `queue` to store all 
#         # the cells to be visited.
#         queue = collections.deque()
#         queue.append([start_row, start_col, 0])
        
#         while queue:
#             curr_row, curr_col, curr_distance = queue.popleft()
            
#             # For the current cell, check its four neighbor cells.
#             for d in dirs:
#                 next_row = curr_row + d[0]
#                 next_col = curr_col + d[1]
                
#                 # If there exists an unvisited empty neighbor:
#                 if 0 <= next_row < rows and 0 <= next_col < cols \
#                     and maze[next_row][next_col] == ".":
                    
#                     # If this empty cell is an exit, return distance + 1.
#                     if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
#                         return curr_distance + 1
                    
#                     # Otherwise, add this cell to 'queue' and mark it as visited.
#                     maze[next_row][next_col] = "+"
#                     queue.append([next_row, next_col, curr_distance + 1])
            
#         # If we finish iterating without finding an exit, return -1.
#         return -1