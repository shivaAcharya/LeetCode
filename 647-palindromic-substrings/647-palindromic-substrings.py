class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        ##################### EXPANDING AROUND THE CENTER #######################
        
        Algorithm:
        1.  Initialize res to 0.
        2.  Iterate over s:
        3.      For every element increment the res.
        4.      Check if it can be expanded around that element, increment res if possible.
        5.  Return res 
                
        """
        
        res = 0
        
        for i in range(len(s)):
            l = r = i
            # Handle odd palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            # Handle evev palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res
        
        """
        DRY RUN:
        2. aaaa
        i = 0
        res = 1
        
        
        
        
        """