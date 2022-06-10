class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = max_length = 0
        for r, c in enumerate(s):
            if c in last_seen:
                l = max(l, last_seen[c] + 1)
            max_length = max(max_length, r - l + 1)
            last_seen[c] = r
        
        return max_length        