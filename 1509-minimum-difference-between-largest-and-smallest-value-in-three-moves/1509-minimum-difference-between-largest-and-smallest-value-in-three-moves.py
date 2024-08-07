"""
[1,5,0,10,14]

[0, 1, 2, 3, 5, 10, 12, 13, 14]


[1,5,0,10,14]

[20, 75, 81, 82, 95]

"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)

        # If the array has 4 or fewer elements, return 0
        if nums_size <= 4:
            return 0

        nums.sort()

        min_diff = float("inf")

        # Four scenarios to compute the minimum difference
        for left in range(4):
            right = nums_size - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])

        return min_diff