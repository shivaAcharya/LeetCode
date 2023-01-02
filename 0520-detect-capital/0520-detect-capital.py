class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.islower(): return True
        
        return word.isupper() or word.istitle()