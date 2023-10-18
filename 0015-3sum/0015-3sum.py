class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sorting, two pointer, skipping duplicates
        
        1. Sort nums
        2. Use two pointer technique to find sum to be 0
        3.      Skip duplicates when occur
        
        '''
        
        nums.sort()
        res = []
        
        for i, num in enumerate(nums):
            
            if i > 0 and nums[i - 1] == num:
                continue
                
            # Two pointer technique
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                
                cur_sum = num + nums[l] + nums[r]
                
                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    
                if cur_sum > 0:
                    r -= 1
                else:
                    l += 1
                    # discard duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res