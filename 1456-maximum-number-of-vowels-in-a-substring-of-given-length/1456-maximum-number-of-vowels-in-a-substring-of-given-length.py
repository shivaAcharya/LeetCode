class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = wind_vowels = 0
        left = 0
        
        for right, letter in enumerate(s):
            if right < k:
                if letter in VOWELS:
                    wind_vowels += 1
                    max_vowels = max(max_vowels, wind_vowels)
                continue
            # Consider letter
            if letter in VOWELS:
                wind_vowels += 1
            # Move left pointer
            if s[left] in VOWELS:
                wind_vowels -= 1
            left += 1
            max_vowels = max(max_vowels, wind_vowels)
        
        return max_vowels