class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float("inf")
        
        for i, num in enumerate(nums):
            
            # Use two pointers
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur_diff = target - (num + nums[l] + nums[r])
                
                if cur_diff == 0:
                    return target
                
                if abs(cur_diff) <= abs(min_diff):
                    min_diff = cur_diff
                
                if cur_diff > 0:
                    l += 1
                else:
                    r -= 1
        
        return target - min_diff
    