class Solution:
    def maxScore(self, s: str) -> int:
        
        score = 0
        
        for i in range(len(s) - 1):
            score = max(score, s[:i + 1].count('0') + s[i + 1:].count('1'))
        
        return score
    