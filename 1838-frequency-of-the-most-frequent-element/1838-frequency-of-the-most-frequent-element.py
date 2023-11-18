class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = ans = curr = 0
        
        for right, num in enumerate(nums):
            curr += num
            
            # Move left pointer
            while (right - left + 1) * num - curr > k:
                curr -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    