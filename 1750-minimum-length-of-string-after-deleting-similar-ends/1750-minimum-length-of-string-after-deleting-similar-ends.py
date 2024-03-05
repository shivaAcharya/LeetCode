"""
s = "a a b c c a b b a"
           l   r

"""

class Solution:
    def minimumLength(self, s: str) -> int:
        
        l, r = 0, len(s) - 1
        
        while l < r and s[l] == s[r]:
            
            # if s[l] != s[r]:
            #     break
            
            # Move left pointer
            l += 1
            while l < r and s[l] == s[l - 1]:
                l += 1
                
            # Move right pointer
            r -= 1
            while l < r and s[r] == s[r + 1]:
                r -= 1
            
        return r - l + 1
        