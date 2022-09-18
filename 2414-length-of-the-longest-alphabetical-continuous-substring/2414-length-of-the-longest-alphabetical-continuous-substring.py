class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        '''
        Sliding Window
        '''
        
        l, res = 0, 1
        
        for r in range(1, len(s)):
             
            if ord(s[r]) - ord(s[r-1]) != 1:
                l = r
            
            cur_window = r - l + 1
            
            res = max(res, cur_window)
                
        
        return res