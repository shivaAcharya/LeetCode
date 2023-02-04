class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        L = len(nums)

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, L - 1
            while l < r:
                cur_sum = nums[l] + nums[r] + num
                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])

                if nums[l] + nums[r] + num > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
"""
nums = [-4, -1, -1, 0, 1, 2]

"""