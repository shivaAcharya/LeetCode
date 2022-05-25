class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1.  Iterate over all rows and cols and do dfs.
        2.  DFS:
        
        
        """
        self.found = False
        def dfs(row, col, idx):  
            if self.found: return
            
            if idx == len(word):
                self.found = True
                return
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#' or board[row][col] != word[idx]:
                return
                 
            # Store current letter on temp variable to restore 
            tmp = board[row][col]
            
            # Mark current cell as visited
            board[row][col] = '#'
            
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + r, col + c, idx + 1)
            
            board[row][col] = tmp
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, 0)
                    
        return self.found