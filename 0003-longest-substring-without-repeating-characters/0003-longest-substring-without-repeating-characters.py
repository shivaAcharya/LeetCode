"""
max_length = 3
window = {a = 3, 
          b = 2, 
          c = 5}
move_l = max(l, window[s[l]] + 1)

    0 1 2 3 4 5 6 7
s = a b c a b c b b
              l
                 r

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        r = len(s) - 1
        window = {}
        
        for r, c in enumerate(s):
            if c in window:
                l = max(l, window[c] + 1)
            window[c] = r
            res = max(res, r - l + 1)
        
        return res
        