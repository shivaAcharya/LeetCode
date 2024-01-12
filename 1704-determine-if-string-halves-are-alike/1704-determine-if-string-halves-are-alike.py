class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = "aeiouAEIOU"
        L = len(s)
        left_vowel = right_vowel = 0
        
        l, r = 0, L // 2
        
        while r < L:
            if s[l] in VOWELS:
                left_vowel += 1
            if s[r] in VOWELS:
                right_vowel += 1
            l += 1
            r += 1
        
        return left_vowel == right_vowel
        