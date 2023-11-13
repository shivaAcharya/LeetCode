class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        
        vowel_list = [c for c in s if c in vowels]
        vowel_sorted_list = sorted(vowel_list, reverse=True)
        
        res = []
        
        for c in s:
            if c in vowels:
                res.append(vowel_sorted_list.pop())
            else:
                res.append(c)
        
        return "".join(res)
    