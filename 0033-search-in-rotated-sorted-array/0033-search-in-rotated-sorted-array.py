class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Find pivot
        l, r = 0, len(nums) -  1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        # Check pivot
        idx = l
        l, r = 0, len(nums) - 1
        if nums[r] >= target:
            l = idx
        else:
            r = idx
            
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l if nums[l] == target else -1
            