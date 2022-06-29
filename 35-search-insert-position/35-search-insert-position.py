class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Handle edge cases
        # if target < nums[0]: return 0
        # if target > nums[-1]: return len(nums)
        
        # Binary Search
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid
        
        return l