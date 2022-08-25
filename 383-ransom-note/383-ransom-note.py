class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count, mag_count = Counter(ransomNote), Counter(magazine)
        
        for c, count in ran_count.items():
            if count > mag_count[c]:
                return False
        
        return True