class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                
                if cur_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                if cur_sum > 0:
                    k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            
        return res
                