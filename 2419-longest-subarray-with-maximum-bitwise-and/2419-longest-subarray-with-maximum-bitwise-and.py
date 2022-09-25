class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # HINT 1 : Notice that the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers.
        
        # HINT 2 : What does that tell us about the nature of the subarray that we should choose?
        
        # Find the maximum in the nums
        
        # Calculate the length of consecutive maximums
        
        max_num = max(nums)
        
        res = length = 0
        
        for num in nums:
            if num == max_num: 
                length += 1
            else: 
                length = 0
            
            res = max(res, length)
        
        return res