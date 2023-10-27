class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Iterate over s
            Use two pointer to check for palindrom expanding around the center
            Look out for odd/even possibility
        
        '''
        res = ""
        for i in range(len(s)):
            l = r = i
            
            # Check for palindromicity odd case
            while r < len(s) and l >= 0 and s[l] == s[r]:
                l -= 1
                r += 1
            
            if len(res) < r - l - 1:
                res = s[l + 1: r]
                
            # Check for palindromicity even case
            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                l -= 1
                r += 1
                
            if len(res) < r - l - 1:
                res = s[l + 1: r]
        
        return res
        
        '''
        bacad
        res = b
        i = 0
            l = -1
            r = 1
        
        
        '''