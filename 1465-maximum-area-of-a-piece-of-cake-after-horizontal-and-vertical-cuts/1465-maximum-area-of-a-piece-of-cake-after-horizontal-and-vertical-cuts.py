class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_length = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        
        for i in range(1, len(horizontalCuts)):
            max_length = max(max_length, horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i-1])
        
        return (max_length * max_width) % (10**9 + 7)
        