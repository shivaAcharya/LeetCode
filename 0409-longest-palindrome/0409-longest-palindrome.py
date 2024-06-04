class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_counted = False
        counter = Counter(s)
        res = 0
        
        for c in s:
            c_count = counter[c]
            if c_count % 2 == 0:
                res += c_count
            elif not odd_counted:
                res += c_count
                odd_counted = True
            else:
                res += (c_count - 1)
            del counter[c]
        
        return res
        