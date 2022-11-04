class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        VOWELS = "aeiouAEIOU"
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and s[l] not in VOWELS:
                l += 1
            while l < r and s[r] not in VOWELS:
                r -= 1
            s_list[l], s_list[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return "".join(s_list)