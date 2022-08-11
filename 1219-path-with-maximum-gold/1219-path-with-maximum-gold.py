class Solution:
    '''
    0 6 0
    5 8 7
    0 9 0
    '''
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.res = 0

        def explore(row, col, gold):
            temp = grid[row][col]
            gold += temp
            self.res = max(self.res, gold)
            grid[row][col] = 0

            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c]:
                    explore(r, c, gold)

            grid[row][col] = temp


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    explore(r, c, 0)

        return self.res