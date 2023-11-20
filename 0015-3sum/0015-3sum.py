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
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:            
                cur_sum = num + nums[l] + nums[r]
                
                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    
                if cur_sum < 0:
                    l += 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res
            