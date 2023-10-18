class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. Find the pivot point using BS
        2. Find the index of target with BS
        '''
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        # Find the right sub-array
        if nums[l] == target:
            return l
        
        left, right = 0, len(nums) - 1
        
        if nums[right] >= target:
            left = l
        else:
            right = l
            
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
            if nums[left] == target:
                return left
                
        return -1
    