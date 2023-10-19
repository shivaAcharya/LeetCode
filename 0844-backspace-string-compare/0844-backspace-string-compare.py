class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        "y#fo##f"           "y#f#o##f"
               ^                    ^
        
        1. Assign s_ptr to last idx of s and t_ptr to last idx of t.
        2. Iterate until s_ptr and t_ptr is greater than -1
        3.      If s_ptr is pointing to #, increment bs_count by 1
        4.          Move s_ptr to left until bs_count is 0
        5.      Repeat 3. and 4. for t_ptr
        6.      Compare letters at s_ptr and t_ptr, return false if not equal.
        7.      Decrement s_ptr and t_ptr by 1
        
        '''
        
        s_ptr, t_ptr = len(s) - 1, len(t) - 1
        
        while s_ptr >= 0 or t_ptr >= 0:
            
            bs_count = 0
            while s_ptr >= 0 and (bs_count > 0 or s[s_ptr] == '#'):
                if s[s_ptr] == '#':
                    bs_count += 1
                else:
                    bs_count -= 1
                s_ptr -= 1
            
            bs_count = 0
            while t_ptr >= 0 and (bs_count > 0 or t[t_ptr] == '#'):
                if t[t_ptr] == '#':
                    bs_count += 1
                else:
                    bs_count -= 1
                t_ptr -= 1
                
            if s_ptr >= 0 and t_ptr >= 0:
                if s[s_ptr] != t[t_ptr]:
                    return False
                
            s_ptr -= 1
            t_ptr -= 1
        
        return s_ptr == t_ptr
                