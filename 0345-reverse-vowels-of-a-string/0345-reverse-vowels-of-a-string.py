class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        VOWELS = "aeiouAEIOU"
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] not in VOWELS:
                l += 1
            if s[r] not in VOWELS:
                r -= 1
            if s[l] in VOWELS and s[r] in VOWELS:
                s_list[l], s_list[r] = s[r], s[l]
                l += 1
                r -= 1
        
        return "".join(s_list)