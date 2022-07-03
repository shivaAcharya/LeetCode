class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        next_neg = next_pos = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if next_pos:
                    next_pos, next_neg = False, True
                    res += 1
            elif nums[i] < nums[i-1]:
                if next_neg:
                    next_neg, next_pos = False, True
                    res += 1
        
        return res
"""
        0 1  2 3  4  5  6  7  8 9 
nums = [1,17,5,10,13,15,10,5,16,8]
res = 4
left = 0
next_neg = T
next_pos = F

i = 4


"""
                