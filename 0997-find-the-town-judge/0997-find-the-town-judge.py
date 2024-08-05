class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Base case
        if n == 1: return n

        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for cand, score in enumerate(trust_scores):
            if score == n - 1:
                return cand

        return -1
    