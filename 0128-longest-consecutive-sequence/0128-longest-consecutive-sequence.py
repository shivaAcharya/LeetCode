'''
1. Create a nums_set from nums for O(1) lookups
2. Find the smallest element and calculate cur_sequence.
3. Maitain lcs
4. Return lcs
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        lcs = 0

        for num in nums:
            count = 1
            if num - 1 not in nums_set:
                while num + 1 in nums_set:
                    count += 1
                    num += 1
            
            lcs = max(lcs, count)
        
        return lcs
        