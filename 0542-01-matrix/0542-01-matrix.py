class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        seen = set()
        Q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if not mat[r][c]:
                    seen.add((r, c))
                    Q.append((r, c))
        
        distance = 1
        while Q:
            for _ in range(len(Q)):
                r, c = Q.popleft()
                for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen:
                        mat[row][col] = distance
                        Q.append((row, col))
                        seen.add((row, col))
            
            distance += 1
        
        return mat
    