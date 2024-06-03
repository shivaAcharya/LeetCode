"""
res = 5
s_ptr = 0
t_ptr = 0
S = 8
T = 6

                       v
s = "coaching", t = "coding"
       ^                    
                  v
s = "vrykt", t = "rkge"
     ^  
       
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = 0
        s_ptr = t_ptr = 0
        S, T = len(s), len(t)
        
        while s_ptr < S:
            s_pt = s_ptr
            if s[s_ptr] == t[t_ptr]:
                while s_pt < S and t_ptr < T:
                    if s[s_pt] == t[t_ptr]:
                        t_ptr += 1
                    s_pt += 1
                    res = max(res, t_ptr)
            t_ptr = 0
            s_ptr = s_pt if s_ptr != s_pt else s_pt + 1
        
        return T - res
        