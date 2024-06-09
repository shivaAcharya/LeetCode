class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []
        
        def backtrack(i, cur_sum):
            if cur_sum == 0:
                res.append(candidate[:])
                return
            
            if cur_sum < 0 or i >= len(candidates):
                return
            
            # Decision to include nums[i]
            candidate.append(candidates[i])
            backtrack(i, cur_sum - candidates[i])
            
            # Decision to NOT include nums[i]
            candidate.pop()
            backtrack(i + 1, cur_sum)
    
        backtrack(0, target)
        return res
    