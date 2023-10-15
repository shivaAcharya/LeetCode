class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. Sort nums.
        2. For every num in nums:
        3.  # Two pointer technique to find sum = 0
        4.  # Skip duplicates
        
        '''
        
        nums.sort()
        L = len(nums)
        res = []
        
        for i, num in enumerate(nums):

            # Check for duplicates
            if i > 0 and nums[i - 1] == num:
                continue
            
            # Two pointer
            l, r = i + 1, L - 1
            
            while l < r:
                # Skip duplicates
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r < L - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                
                cur_sum = num + nums[l] + nums[r]
                
                # Check for 0 sum
                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                
                # Move pointer based on sum
                if cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
        
        '''
        [-4, -1, -1, 0, 1, 2]
        
        [-1,-1,0,1]
        L = 4
        
        '''
        