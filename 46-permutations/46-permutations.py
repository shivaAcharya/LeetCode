class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        
        def backtrack(lst):
            if len(perm) == len(nums):
                res.append(perm[:])
            
            for i, candidate in enumerate(lst):
                perm.append(candidate)
                backtrack(lst[:i] + lst[i+1:])
                perm.pop()
        
        backtrack(nums)
        return res