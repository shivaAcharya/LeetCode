class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        a, b = edges[0][0], edges[0][1]
        c, d = edges[1][0], edges[1][1]
        
        if a == c:
            return a
        if b == c:
            return b
        return d
            