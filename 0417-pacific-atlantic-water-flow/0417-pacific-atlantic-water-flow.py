"""
Initialize P_Q, A_Q, P_Set, and A_Set with first and last row and column elements
Perform BFS on P_Q and populate P_Set meeting given conditions.
DO step 2 on A_Q
Return P_Set intersection with A_Set
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        P_Q, A_Q, P_Set, A_Set = deque(), deque(), set(), set()

        # Populate P_Q and P_Set
        for c in range(COLS):
            P_Q.append((0, c))
            P_Set.add((0, c))
        
        for r in range(ROWS):
            P_Q.append((r, 0))
            P_Set.add((r, 0))

        # Populate A_Q and A_Set
        for c in range(COLS):
            A_Q.append((ROWS - 1, c))
            A_Set.add((ROWS - 1, c))
        
        for r in range(ROWS):
            A_Q.append((r, COLS - 1))
            A_Set.add((r, COLS - 1))

        # Perform BFS on P_Q
        while P_Q:
            r, c = P_Q.popleft()

            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in P_Set and heights[r][c] <= heights[nr][nc]:
                    P_Q.append((nr, nc))
                    P_Set.add((nr, nc))
        
        # Perform BFS on A_Q
        while A_Q:
            r, c = A_Q.popleft()

            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in A_Set and heights[r][c] <= heights[nr][nc]:
                    A_Q.append((nr, nc))
                    A_Set.add((nr, nc))
        
        res = []
        for (r, c) in P_Set:
            if (r, c) in A_Set:
                res.append([r, c])
        
        return res

"""
Time => O(MN)
Space => O(MN)
"""