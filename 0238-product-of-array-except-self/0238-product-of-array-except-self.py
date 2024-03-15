class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        
        for i in range(1, len(nums)):
            prod[i] = prod[i - 1] * nums[i - 1]
        
        cur_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            cur_prod *= nums[i + 1]
            prod[i] *= cur_prod

        return prod
        