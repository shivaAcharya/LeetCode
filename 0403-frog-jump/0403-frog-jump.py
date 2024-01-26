class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        mark = {}
        # Mark stones in the map to identify if such stone exists or not.
        for i in range(len(stones)):
            mark[stones[i]] = i
        
        # Initialize with -1s to denote they are not calculated
        dp = [[-1] * 2001 for _ in range(2001)]
        
        def solve(idx, prev_jump):
            # If reached the last stone, return True
            if idx == len(stones) - 1:
                return True
            
            # If this subproblem has already been calculated, return it.
            if dp[idx][prev_jump] != -1:
                return dp[idx][prev_jump] == 1
            
            ans = False
            # Iterate over three possibilities {k - 1, k, k + 1}
            for nxt_jump in (prev_jump - 1), (prev_jump), (prev_jump + 1):
                if nxt_jump > 0 and stones[idx] + nxt_jump in mark:
                    nxt_idx = mark[stones[idx] + nxt_jump]
                    ans = ans or solve(nxt_idx, nxt_jump)
            
            # Store the result to fetch later
            dp[idx][prev_jump] = 1 if ans else 0
            return ans          
            
        return solve(0, 0)
    