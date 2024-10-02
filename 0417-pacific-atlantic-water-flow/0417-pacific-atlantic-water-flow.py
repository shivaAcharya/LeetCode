class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        A_Q, P_Q, A_Set, P_Set = deque(), deque(), set(), set()
        
        # Poplulate P_Q
        for r in range(ROWS):
            P_Q.append((r, 0))
            P_Set.add((r, 0))
            
        for c in range(COLS):
            P_Q.append((0, c))
            P_Set.add((0, c))
            
        # Populate A_Q
        for r in range(ROWS):
            A_Q.append((r, COLS - 1))
            A_Set.add((r, COLS - 1))
            
        for c in range(COLS):
            A_Q.append((ROWS - 1, c))
            A_Set.add((ROWS - 1, c))
        
        # Iterate over P_Q
        while P_Q:
            r, c = P_Q.popleft()
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in P_Set and heights[nr][nc] >= heights[r][c]:
                    P_Set.add((nr, nc))
                    P_Q.append((nr, nc))
        
        # Iterate over A_Q
        while A_Q:
            r, c = A_Q.popleft()
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in A_Set and heights[nr][nc] >= heights[r][c]:
                    A_Set.add((nr, nc))
                    A_Q.append((nr , nc))
                    
        res = []
        # print(A_Set, P_Set)
        for r, c in P_Set:
            if (r, c) in A_Set:
                res.append([r, c])       
        return res