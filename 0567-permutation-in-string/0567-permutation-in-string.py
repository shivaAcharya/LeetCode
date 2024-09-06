class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_count = defaultdict(int)        
        s1_count = Counter(s1)
        
        l = 0
        for r, c in enumerate(s2):
            s2_count[c] += 1
            
            if s1_count == s2_count: return True
            if r < len(s1) - 1: continue
            
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            l += 1
        
        return False
        