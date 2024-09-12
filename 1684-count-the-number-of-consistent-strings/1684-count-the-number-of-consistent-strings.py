class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        consistent_str = 0
        
        for word in words:
            for c in word:
                if c not in allowed:
                    break
            else:
                consistent_str += 1
        
        return consistent_str
    