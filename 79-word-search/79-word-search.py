class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Input validating
        if not word or not board:
            return False

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, ptr):
            if ptr == len(word):
                return True

            if not 0 <= r < ROWS or not 0 <= c < COLS:
                return False

            if board[r][c] != word[ptr]:
                return False

            temp = board[r][c]
            board[r][c] = ""
            for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if dfs(row, col, ptr+1):
                    return True
            board[r][c] = temp
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False