class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        source_color = image[sr][sc]
        Q = deque([(sr, sc)])
        seen = set([(sr, sc)])
        while Q:
            for _ in range(len(Q)):
                r, c = Q.popleft()
                image[r][c] = color
                for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and image[row][col] == source_color:
                        Q.append((row, col))
                        seen.add((row, col))
                        
        return image
        