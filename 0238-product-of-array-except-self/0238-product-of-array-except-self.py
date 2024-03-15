class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod, right_prod = [1] * len(nums), [1] * len(nums)
        
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
            
        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]
        # print(left_prod, right_prod)
        return [num1 * num2 for num1, num2 in zip(left_prod, right_prod)]
        