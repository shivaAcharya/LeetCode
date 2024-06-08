class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        
        def dfs(i):
            
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision to NOT include nums[i]
            subset.pop()
            dfs(i + 1)
        
        
        dfs(0)
        return res
        