class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited:
                    break
                    
                visited.add((r, c))
                
                cur_elements = []
                
                # Traverse diagonal
                i, j = r, c
                while 0 <= i < ROWS and 0 <= j < COLS:
                    cur_elements.append(mat[i][j])
                    i += 1
                    j += 1
                
                cur_elements.sort()
                idx = 0
                i, j = r, c
                while 0 <= i < ROWS and 0 <= j < COLS:
                    mat[i][j] = cur_elements[idx]
                    i += 1
                    j += 1
                    idx += 1
                    
        return mat