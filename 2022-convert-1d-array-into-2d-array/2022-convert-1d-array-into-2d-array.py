class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Edge case
        if len(original) != m * n: return []
        
        res = [[0] * n for _ in range(m)]
        index = 0
        
        for i in range(m):
            for j in range(n):
                print(i, j)
                res[i][j] = original[index]
                index += 1
                
        return res
    