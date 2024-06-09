# 
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix_mod = res = 0
        
        mod_groups = [0] * k
        mod_groups[0] = 1
        
        # There are k mod groups, 0.....k-1.
        for num in nums:
            # Take modulo twice to avoid negative remainders
            prefix_mod = (prefix_mod + num % k + k) % k
            
            # Add the count of subarrays that have the same remainder as the current
            res += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1
        
        return res