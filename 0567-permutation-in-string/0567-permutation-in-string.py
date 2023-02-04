class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s1_length = len(s1)
        
        for i in range(len(s2)):
            if s1_counter == Counter(s2[i : i + s1_length]):
                return True
        
        return False