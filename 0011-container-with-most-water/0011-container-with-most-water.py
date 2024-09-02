"""
          0  1  2  3  4  5  6  7  8
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
                l               
                                  r

area = height x width
max_area = 49
cur_area = min(height[l], height[r]) * (r - l)
cur_area = 8, 49, 42, 15,

[1, 2, 4, 3]
    l
          r
          
[1, 3, 2, 5, 25, 24, 5]
    l
                     r
area = 15

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur_area = max_area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, cur_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
    