class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. Find the pivot point using BS
        2. Find the index of target with BS
        '''
        
        # Find pivot idx
        l, r = 0, len(nums) - 1

        # [1, 2]
        #  ^
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid

        # pivot idx = l
        pivot_idx = l
        if nums[l] == target:
            return l

        l, r = 0, len(nums) - 1
        if target > nums[-1]:
            r = pivot_idx - 1
        else:
            l = pivot_idx + 1

        # [1, 2 2]
        # ^
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
    