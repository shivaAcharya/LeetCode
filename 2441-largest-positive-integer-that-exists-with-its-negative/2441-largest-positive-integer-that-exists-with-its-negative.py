class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums.sort()
        
        for num in reversed(nums):
            if -num in nums_set:
                return num
        
        return -1
        