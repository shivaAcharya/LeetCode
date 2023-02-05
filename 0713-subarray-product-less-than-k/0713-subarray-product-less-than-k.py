class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        count = left = 0
        
        for right, num in enumerate(nums):
            product *= num
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        
        return count