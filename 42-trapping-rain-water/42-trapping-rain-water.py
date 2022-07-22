class Solution:
    def trap(self, height: List[int]) -> int:
        # Calculate running_max from the end
        max_right = [0] * len(height)
        max_right[-1] = height[-1]
        
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        
        
        # Calculate running_max from front and water
        water = 0
        max_so_far = 0
        
        for i in range(len(height) - 1):
            max_so_far = max(max_so_far, height[i])
            water += min(max_so_far, max_right[i]) - height[i]
        
        return water


