class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        changed = False
        
        for i in range(len(nums) - 1):
            
            if nums[i+1] < nums[i]:
                
                if changed:
                    return False
                
                # [3, 4, 2, 3]
                if i > 0 and nums[i+1] < nums[i-1]:
                    # change the later one
                    nums[i+1] = nums[i]
                else: # otherwise, change the front one
                    nums[i] = nums[i+1]
                
                changed = True
                
        return True