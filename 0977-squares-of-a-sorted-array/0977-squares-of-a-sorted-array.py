class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # If all elements are either non-negative or non-positive, square each num and return them
        res = []
        if not nums: return res
        if nums[0] >= 0: return [num * num for num in nums]
        if nums[-1] <= 0: return [num * num for num in reversed(nums)]

        L = len(nums)
        left, right = 0, L - 1
        # Find first non-negative num
        for i, num in enumerate(nums):
            if num >= 0:
                left, right = i - 1, i
                break

        while left >= 0 or right < L:

            if left < 0:
                res.append(nums[right] ** 2)
                right += 1
                continue

            if right > L - 1:
                res.append(nums[left] ** 2)
                left -= 1
                continue 

            left_num, right_num = nums[left], nums[right]

            if left_num ** 2 < right_num ** 2:
                res.append(left_num ** 2)
                left -= 1
            else:
                res.append(right_num ** 2)
                right += 1

        return res