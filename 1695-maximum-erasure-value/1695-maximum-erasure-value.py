class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        last_seen = {}

        max_score = window_sum = l = 0

        for r, num in enumerate(nums):

            if num in last_seen:
                new_l = max(l, last_seen[num] + 1)
                # Delete from window_sum
                for i in range(l, new_l):
                    window_sum -= nums[i]

                l = new_l

            last_seen[num] = r
            window_sum += num

            max_score = max(max_score, window_sum)

        return max_score