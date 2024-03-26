class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_elem = max(0, max(nums))
        nums_set = set(nums)
        
        for i in range(1, max_elem):
            if i not in nums_set:
                return i
        
        return max_elem + 1