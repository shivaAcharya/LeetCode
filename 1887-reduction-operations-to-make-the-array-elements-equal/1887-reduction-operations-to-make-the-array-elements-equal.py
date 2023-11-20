class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        factor = 0
        ans = 0
        
        for i, num in enumerate(nums):
            if i == 0 or (factor == 0 and num == nums[i - 1]):
                continue
            if num != nums[i - 1]:
                factor += 1
            
            ans += factor
            
        return ans
    