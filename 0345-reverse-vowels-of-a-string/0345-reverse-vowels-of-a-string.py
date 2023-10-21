class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer to vowel
            while l < r and list_s[l] not in vowels:
                l += 1
                
            # Move right pointer to vowel
            while l < r and list_s[r] not in vowels:
                r -= 1
                
            if l < r:
                list_s[l], list_s[r] = list_s[r], list_s[l]
                l += 1
                r -= 1
        
        return "".join(list_s)