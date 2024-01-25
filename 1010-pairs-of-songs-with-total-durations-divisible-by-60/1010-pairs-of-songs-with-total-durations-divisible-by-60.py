class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        seen = [0] * 60
        res = 0
        for t in time:
            res += seen[(60 - (t % 60)) % 60]
            seen[t % 60] += 1
        
        return res
        