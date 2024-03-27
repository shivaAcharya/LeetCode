class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        prod = 1
        count = left = 0
        
        for right, num in enumerate(nums):
            prod *= num
            
            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
    