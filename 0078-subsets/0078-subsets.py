class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []    # Output lists
        
        subset = [] # Stack to store subset
        
        def dfs(i):
            # Base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return res