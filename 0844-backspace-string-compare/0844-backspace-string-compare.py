class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_ptr, t_ptr = len(s) - 1, len(t) - 1
        
        while s_ptr >= 0 or t_ptr >= 0:
                       
            back_str = 0
            while s_ptr >= 0 and (s[s_ptr] == '#' or back_str):
                if s[s_ptr] == '#':
                    back_str += 1
                else:
                    back_str -= 1
                s_ptr -= 1
            
            
            back_str = 0
            while t_ptr >= 0 and (t[t_ptr] == '#' or back_str):
                if t[t_ptr] == '#':
                    back_str += 1
                else:
                    back_str -= 1
                t_ptr -= 1
                
            
            if s_ptr >= 0 and t_ptr >= 0:
                if s[s_ptr] != t[t_ptr]:
                    return False
                
            s_ptr -= 1
            t_ptr -= 1
        
        return s_ptr == t_ptr