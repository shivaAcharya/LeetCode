class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Sliding Window
        left = count = 0
        product = 1
        
        for right, num in enumerate(nums):
            product *= num
            
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
            