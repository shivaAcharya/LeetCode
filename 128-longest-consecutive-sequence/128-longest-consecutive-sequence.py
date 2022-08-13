class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        max_count = 0
        
        for num in numSet:
            if num - 1 not in numSet:
                
                count = 1
                
                while num + 1 in numSet:
                    count += 1
                    num += 1
                
                max_count = max(max_count, count)
        
        return max_count