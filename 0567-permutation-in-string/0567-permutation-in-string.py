class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed size sliding window
        
        need = Counter(s1)
        have = {}
        left = 0
        for right, c in enumerate(s2):
            have[c] = have.get(c, 0) + 1
            if right < len(s1) - 1:
                continue
            #print(need, have)
            if need == have:
                return True
            have[s2[left]] -= 1
            if have[s2[left]] == 0:
                del have[s2[left]]
            left += 1
        
        return False