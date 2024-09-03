"""
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
prefix = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
postfix = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]

    i = 2
water = min(max_l, max_r) - height[i] => (1) - 0 => 1
    i = 5
        2 - 0 => 2

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        prefix = [0] * L
        postfix = [0] * L
        
        for i in range(1, L):
            prefix[i] = max(height[i - 1], prefix[i - 1])
        
        for i in range(L - 2, -1, -1):
            postfix[i] = max(height[i + 1], postfix[i + 1])
        
        # print(prefix, postfix)
        res = 0
        for i, h in enumerate(height):
            water = max(min(prefix[i], postfix[i]) - h, 0)
            # print()
            res += water
        
        return res
        