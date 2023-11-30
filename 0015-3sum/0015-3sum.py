class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        # [-4, -1, -1, -1, 0, 1, 2]
        
        for i, num in enumerate(nums):
            # Remove duplicates from the first pointer
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            # Use two pointers
            while l < r:
                cur_sum = num + nums[l] + nums[r]
                
                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])
                
                if cur_sum > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res                
        