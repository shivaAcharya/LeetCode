class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        res = [[None] * COLS for _ in range(ROWS)]
        
        # Flip
        for row in range(ROWS):
            l, r = 0, COLS - 1
            while l <= r:
                res[row][l], res[row][r] = image[row][r], image[row][l]
                l += 1
                r -= 1
        
        print(res)
        # Invert
        for r in range(ROWS):
            for c in range(COLS):
                res[r][c] = 1 if res[r][c] == 0 else 0
        
        return res
        