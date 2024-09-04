"""

s = A B A B
    l
      r

k = 2
have = {A:1}

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        res = l = 0
        
        for r, c in enumerate(s):
            window[c] += 1
            
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
    