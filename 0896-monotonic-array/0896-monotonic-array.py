class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        
        is_increasing = None
        
        i = 0
        while i < len(nums) - 1:
            
            if nums[i+1] - nums[i] > 0:
                if is_increasing is None:
                    is_increasing = True
                elif is_increasing == False:
                    return False
            elif nums[i+1] - nums[i] < 0:
                if is_increasing is None:
                    is_increasing = False
                if is_increasing == True:
                    return False
            i += 1
        
        return True