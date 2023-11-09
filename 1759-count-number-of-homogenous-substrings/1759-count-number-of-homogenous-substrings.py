class Solution:
    def countHomogenous(self, s: str) -> int:
        
        res = 0
        cur_streak = 0
        
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                cur_streak += 1
            else:
                cur_streak = 1
                
            res = (res + cur_streak) % (10 ** 9 + 7)
        
        return res
    