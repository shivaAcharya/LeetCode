class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        mark = {}
        dp = [[-1] * 2001 for _ in range(2001)]
        
        def solve(idx, prev_jump):
            
            if idx == len(stones) - 1:
                return True
            
            if dp[idx][prev_jump] != -1:
                return dp[idx][prev_jump] == 1
            
            ans = False
            for nxt_jump in (prev_jump - 1), (prev_jump), (prev_jump + 1):
                if nxt_jump > 0 and stones[idx] + nxt_jump in mark:
                    nxt_idx = mark[stones[idx] + nxt_jump]
                    ans = ans or solve(nxt_idx, nxt_jump)
            
            dp[idx][prev_jump] = 1 if ans else 0
            return ans
        
        for i in range(len(stones)):
            mark[stones[i]] = i           
            
        return solve(0, 0)
    