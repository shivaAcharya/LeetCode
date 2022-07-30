class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.res = ""
        
        def helper(l, r):
            
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1         
            if r - l - 1 > len(self.res):
                self.res = s[l+1:r]
            
        
        for i in range(len(s)):
            helper(i, i)       # For odd length
            helper(i, i + 1)   # For even length
        
        return self.res