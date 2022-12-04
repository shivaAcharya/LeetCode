class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        L = len(nums)
        right_sum = [0] * L
        
        # Calculate running sum from the right 
        for i in range(L - 2, -1, -1):
            right_sum[i] += right_sum[i+1] + nums[i+1]
        
        left_sum = min_idx = 0
        min_avg = float("inf")
        for i, num in enumerate(nums):
            left_sum += num
            right_num = (L - i - 1)
            if not right_num:
                right_num = 1
            average = abs(left_sum // (i + 1) - (right_sum[i] // right_num))
            if average < min_avg:
                min_avg, min_idx = average, i
        
        return min_idx