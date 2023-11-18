class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
#         nums.sort()
        
#         nums_diff = []
        
#         for i in range(1, len(nums)):
#             nums_diff.append(nums[i] - nums[i - 1])
        
#         freq = 1
        
#         while nums_diff and k > 0:
#             k -= heapq.heappop(nums_diff)
#             if k >= 0:
#                 freq += 1
            
#         return freq
        nums.sort()
        n = len(nums)
        left, right = 0, 0
        max_freq = 0
        current_sum = 0

        while right < n:
            current_sum += nums[right]

            while (right - left + 1) * nums[right] - current_sum > k:
                current_sum -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)
            right += 1

        return max_freq