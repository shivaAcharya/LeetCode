"""
Find pivot index
Figure out what side of pivot index is the target located
Find the target element

               l
               m
                    r
nums = [4,5,6,7,0,1,2], target = 0


"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find Pivot index
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        # print(l)
        # Check Pivot
        idx = l
        l, r = 0, len(nums) - 1
        if nums[r] >= target:
            l = idx
        else:
            r = idx
        
        # print(l, r)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l if nums[l] == target else -1
"""
[1, 3]


"""    