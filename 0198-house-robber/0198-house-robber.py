'''
            / \
           0   1 
          /\  / \
         2 3 3

0 -> 2 => 4
0 -> 3 => 2
1 -> 3 => 3


'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        prev, last = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            prev, last = last, max(nums[i] + prev, last)
        
        return last
        
#         memo = {}
#         def dp(i):
#             if i >= len(nums):
#                 return 0
            
#             if i not in memo:
#                 memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            
#             return memo[i]
        
#         return dp(0)