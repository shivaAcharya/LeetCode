"""
nums = [1, 2, 3, 1]

   1        2
3     1   1

maximize money
cannot rob two adjacent houses

[2,7,9,3,1]
            start
         /         \ 
        2           7
    9      3    3       1
1              


"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            left = dfs(i + 1)
            right = dfs(i + 2) + nums[i]
            memo[i] =  max(left, right)
            return memo[i]
                    
        return max(dfs(0), dfs(1))
    