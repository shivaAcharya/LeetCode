class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        l = window_sum = 0
        maxi = total - x
        res = float("inf")
        
        for r, num in enumerate(nums):
            window_sum += num
            
            while l <= r and window_sum > maxi:
                window_sum -= nums[l]
                l += 1
            
            if window_sum == maxi:
                res = min(res, n - (r - l + 1))
        
        return res if res != float("inf") else -1