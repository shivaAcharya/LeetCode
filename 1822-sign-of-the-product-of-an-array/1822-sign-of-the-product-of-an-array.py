class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_neg = False
        
        for num in nums:
            if num == 0: return 0
            if num < 0:
                is_neg = not is_neg
        
        return -1 if is_neg else 1