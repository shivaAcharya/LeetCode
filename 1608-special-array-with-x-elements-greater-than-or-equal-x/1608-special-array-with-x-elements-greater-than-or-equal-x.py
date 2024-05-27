"""
[0, 0, 3, 4, 4]

0 -> 4

"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        ptr1 = 0
        L = len(nums)
        
        for i in range(0, L + 1):
            while ptr1 < L and nums[ptr1] < i:
                ptr1 += 1
            
            if i == L - ptr1:
                return i
        
        return -1
        
        