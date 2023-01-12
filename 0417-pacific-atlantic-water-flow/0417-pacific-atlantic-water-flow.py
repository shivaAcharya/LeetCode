class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        P_Q, A_Q, P_S, A_S = deque(), deque(), set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        # Populate P_Q and P_S
        for c in range(COLS):
            P_Q.append((0, c))
            P_S.add((0, c))

        for r in range(ROWS):
            P_Q.append((r, 0))
            P_S.add((r, 0))
        
        # Populate A_Q and A_S
        for c in range(COLS):
            A_Q.append((ROWS - 1, c))
            A_S.add((ROWS - 1, c))
        
        for r in range(ROWS):
            A_Q.append((r, COLS - 1))
            A_S.add((r, COLS - 1))

        # BFS on P_Q
        while P_Q:
            r, c = P_Q.popleft()

            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in P_S and heights[row][col] >= heights[r][c]:
                    P_S.add((row, col))
                    P_Q.append((row, col))

        # BFS on A_Q
        while A_Q:
            r, c = A_Q.popleft()

            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in A_S and heights[row][col] >= heights[r][c]:
                    A_S.add((row, col))
                    A_Q.append((row, col))
        
        # Calculate result
        res = []
        for r, c in P_S:
            if (r, c) in A_S:
                res.append([r, c])
        
        return res 