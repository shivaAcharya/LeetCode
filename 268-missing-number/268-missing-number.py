class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_sum = (n * (n+1)) // 2
        
        return n_sum - sum(nums)