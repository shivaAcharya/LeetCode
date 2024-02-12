"""
    nums = [2, 2, 1, 1, 1, 2, 2] #7
    majority elem

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        counter = {}
        L = len(nums)
        
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
                if counter[num] > L // 2:
                    return num
        