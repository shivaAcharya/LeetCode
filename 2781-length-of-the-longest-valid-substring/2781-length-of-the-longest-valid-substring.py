# https://leetcode.com/problems/length-of-the-longest-valid-substring/discuss/3771333/Picture-Short-and-Concise-Approach-Easy-to-Understand-In-depth-Explanation
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:

        forbidden_set = set(forbidden)
        res = 0
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k+1] in forbidden_set:
                    right = k - 1
                    break
            res = max(res, right - left + 1)
        return res
    