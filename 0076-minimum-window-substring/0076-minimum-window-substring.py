"""
Handle edge case of returning "" when len(t) > len(s).
Initialize count_t and window hashmaps. Also res_len = inf, res = [-1, -1], need = len(t) and have = 0
Populate count_t with chars from t.
# Sliding window technique
for r, c in enumerate(s):
    Add c to window if c in count_t
    check if window[c] == count_t, increment have
    while have == need:
        # update res
        # move left pointer

return s[l : r + 1] if res_len != inf

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""
        
        count_t = Counter(t)
        window = {}
        
        res, res_len = [-1, -1], float("inf")
        have, need = 0, len(count_t)
        l = 0
        # print(count_t)
        for r, c in enumerate(s):
            if c in count_t:
                window[c] = 1 + window.get(c, 0)

                if c in count_t and window[c] == count_t[c]:
                    have += 1

                while have == need:
                    # Update res
                    if (r - l + 1) < res_len:
                        res_len = r - l + 1
                        res = [l, r]

                    # Update l
                    if s[l] in count_t:
                        window[s[l]] -= 1
                        if window[s[l]] < count_t[s[l]]:
                            have -= 1
                    l += 1

        # print(res)
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""          
        
        