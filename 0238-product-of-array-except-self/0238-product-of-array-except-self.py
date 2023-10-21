class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        [1, 2, 3, 4]
        
        left_prod = [1, 1, 2, 6]
        right_prod = [24, 12, 4, 1]
        res = [24, 12, 8, 6]
        
        '''
        L = len(nums)
        right_prod = [1] * L
        res = []
        
        # Populate right_prod
        for i in range(L - 2, -1, -1):
            right_prod[i] = nums[i + 1] * right_prod[i + 1]
        
        # Populate res with left product
        for i in range(L):
            cur_prod = 1 if i == 0 else cur_prod * nums[i - 1]
            res.append(cur_prod * right_prod[i])
        
        return res
            