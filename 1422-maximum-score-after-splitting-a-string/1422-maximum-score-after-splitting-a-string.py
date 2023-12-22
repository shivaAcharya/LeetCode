class Solution:
    def maxScore(self, s: str) -> int:
        
        score = 0
        prefix_max = [0] * (len(s) + 1)
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                prefix_max[i] = prefix_max[i + 1] + 1
            else:
                prefix_max[i] = prefix_max[i + 1]
        
        print(prefix_max)
        zero_count = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_count += 1
            score = max(score, zero_count + prefix_max[i + 1])
        
        return score
    