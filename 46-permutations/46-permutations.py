class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def backtrack(candidates):
            if not candidates:
                res.append(perm[:])
                #perm.clear()
                return
            
            for i, candidate in enumerate(candidates):
                perm.append(candidate)
                backtrack(candidates[:i] + candidates[i+1:])
                perm.pop()
        
        backtrack(nums)
        return res