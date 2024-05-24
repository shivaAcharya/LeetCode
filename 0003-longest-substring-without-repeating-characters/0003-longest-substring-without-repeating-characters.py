class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res = left = 0
        
        for right, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(c)
            res = max(res, right - left + 1)
        
        return res            
        