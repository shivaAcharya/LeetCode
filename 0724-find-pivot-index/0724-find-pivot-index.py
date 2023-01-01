class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        '''
        [1, 2]
        right = [3, 2, 0]
        
        [2, 1, -1]
        
        right = [2, 0, -1, 0]
        
        [1, 7, 3, 6, 5, 6]
        right = [28, 27, 20, 17, 11, 6, 0]
        left = 8
        '''
        
        right = [0] * (len(nums) + 1)
        
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right[i + 1] + nums[i]
            
        left = 0
        for i in range(len(nums)):
                                  
            if left == right[i + 1]:
                return i
            
            left += nums[i]
            
        
        return -1
        
        