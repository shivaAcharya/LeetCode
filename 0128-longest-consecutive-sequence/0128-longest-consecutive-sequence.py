"""
1. Convert nums to nums_set for O(1) lookups
2. Look for the smallest num
3.  Increment count for every num + 1 and maintain max_count.
4. Return max_count
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_count = 0

        for num in nums:
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    count += 1
                    num += 1
                max_count = max(max_count, count)
        
        return max_count
    
"""
Time => O(N)
Space => O(N)
"""