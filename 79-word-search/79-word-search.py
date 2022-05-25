class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1.  Iterate over all rows and cols and do dfs.
        2.  DFS:
        
        
        """
        def dfs(row, col, idx):  
            if idx == len(word):
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#' or board[row][col] != word[idx]:
                return False
                 
            # Store current letter on temp variable to restore 
            tmp = board[row][col]
            
            # Mark current cell as visited
            board[row][col] = '#'
            
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(row + r, col + c, idx + 1):
                    return True
            
            board[row][col] = tmp
            
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
