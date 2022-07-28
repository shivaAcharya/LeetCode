class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        closest_sum = nums[0] + nums[1] + nums[2]
        
        closest = abs(target - closest_sum)
        
        for i in range(len(nums) - 2):
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                
                # Update closest and closest_sum when needed
                if abs(target - cur_sum) < closest:
                    closest = abs(target - cur_sum)
                    closest_sum = cur_sum
                
                if not closest:
                    return closest_sum
                
                # Move pointers
                if target - cur_sum > 0:
                    l += 1
                else:
                    r -= 1
        
        return closest_sum