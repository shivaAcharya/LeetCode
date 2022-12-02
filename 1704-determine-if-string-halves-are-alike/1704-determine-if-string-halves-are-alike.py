class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        VOWELS = "aeiouAEIOU"
        
        l, r = 0, len(s) - 1
        
        left_vowels = right_vowels = 0
        
        while l < r:
            if s[l] in VOWELS:
                left_vowels += 1
            
            if s[r] in VOWELS:
                right_vowels += 1
            
            l += 1
            r -= 1
        
        return left_vowels == right_vowels