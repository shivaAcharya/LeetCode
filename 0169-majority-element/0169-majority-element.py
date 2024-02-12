"""
    nums = [2, 2, 1, 1, 1, 2, 2] #7
    majority elem

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            if count == 0: candidate = num
            
            if num == candidate: 
                count += 1 
            else: 
                count -= 1
        
        return candidate