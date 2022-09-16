class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        ''' 
        self.max_score = float("-inf")
        self.memo = {}
        
        def recurse(cur_score, idx, l, r):
            if idx in self.memo and self.memo[idx] > cur_score:
                return float("-inf")
            
            if idx == len(multipliers):
                self.max_score = max(self.max_score, cur_score)
                return float("-inf")
            
            left = recurse(cur_score + (multipliers[idx] * nums[l]), idx + 1, l + 1, r)
            
            right = recurse(cur_score + (multipliers[idx] * nums[r]), idx + 1, l, r - 1)
            
            self.memo[idx] = max(left, right)
            
            return self.memo[idx]
            
        
        recurse(0, 0, 0, len(nums) - 1)
        
        return self.max_score
        '''
        
        m = len(multipliers)
        n = len(nums)

        dp = [0] * (m + 1)

        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            # Present Row is now next_Row because we are moving upwards

            for left in range(op, -1, -1):

                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])

        return dp[0]