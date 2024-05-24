"""
           l  
s = "a b c a b c b b"
                 r
res = 2
cur_wind = {
    a : 3,
    b : 4,
    c : 5,
}
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = left = 0
        last_seen = {}
        
        for right, c in enumerate(s):
            if c in last_seen:
                left = max(last_seen[c] + 1, left)
            last_seen[c] = right
            res = max(res, right - left + 1)
        
        return res

"""
"abba"

a => 0
b => 1

"""