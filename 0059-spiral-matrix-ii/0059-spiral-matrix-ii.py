class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        layers = (n + 1) // 2
        res = [[None] * n for _ in range(n)]
        count = 1
        
        for layer in range(layers):
            
            # Direction 1 => Traverse from left to right
            for i in range(layer, n - layer):
                res[layer][i] = count
                count += 1
            
            # Direction 2 => Traverse from top to bottom
            for i in range(layer + 1, n - layer):
                res[i][n - layer - 1] = count
                count += 1
            
            # Direction 3 => Traverse from right to left
            for i in range(layer + 1, n - layer):
                res[n - layer - 1][n - i - 1] = count
                count += 1
            
            # Direction 4 => Traverse from bottom to top
            for i in range(layer + 1, n - layer - 1):
                res[n - i - 1][layer] = count
                count += 1
        
        return res