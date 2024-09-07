class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        count_t = Counter(t)
        window = {}
        res, res_len = [-1, -1], float("inf")
        need, have = len(count_t), 0
        
        l = 0
        for r, c in enumerate(s):
            if c in count_t:
                window[c] = 1 + window.get(c, 0)
                
                if window[c] == count_t[c]:
                    have += 1
                    
                while need == have:
                    if (r - l + 1) < res_len:
                        res_len = r - l + 1
                        res = [l, r]
                    
                    if s[l] in count_t:
                        window[s[l]] -= 1
                        if window[s[l]] < count_t[s[l]]:
                            have -= 1
                    l += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
        