class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_diff = float("inf")
        
        for i in range(len(nums)):
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur_diff = target - nums[i] - nums[l] - nums[r]
                
                # If cur_diff is zero, just return target
                if cur_diff == 0:
                    return target
                
                # Update min_diff when needed
                if abs(cur_diff) < abs(min_diff) or (abs(cur_diff) == abs(min_diff)):
                    min_diff = cur_diff
                
                if cur_diff > 0:
                    l += 1
                else:
                    r -= 1
        
        return target - min_diff