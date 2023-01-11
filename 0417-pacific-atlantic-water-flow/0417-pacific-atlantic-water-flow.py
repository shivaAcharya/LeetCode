class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific_Q, atlantic_Q = deque(), deque()
        pacific_set, atlantic_set = set(), set()

        # Populate Qs
        # Add top row
        for c in range(COLS):
            pacific_Q.append((0, c))
        
        # Add first col
        for r in range(ROWS):
            pacific_Q.append((r, 0))

        # Add last row
        for c in range(COLS):
            atlantic_Q.append((ROWS - 1, c))
        
        # Add last col
        for r in range(ROWS):
            atlantic_Q.append((r, COLS - 1))
        
        while pacific_Q:
            row, col = pacific_Q.popleft()

            pacific_set.add((row, col))

            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in pacific_set and heights[r][c] >= heights[row][col]:
                    pacific_Q.append((r, c))
        
        while atlantic_Q:
            row, col = atlantic_Q.popleft()

            atlantic_set.add((row, col))

            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in atlantic_set and heights[r][c] >= heights[row][col]:
                    atlantic_Q.append((r, c))
        
        res = []
        for (r, c) in pacific_set:
            if (r, c) in atlantic_set:
                res.append([r, c])
        
        return res