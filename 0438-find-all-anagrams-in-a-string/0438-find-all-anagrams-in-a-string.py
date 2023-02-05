class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Sliding Window Technique
        need = Counter(p)
        have, left = {}, 0
        res = []
        for right, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            
            if right < len(p) - 1:
                continue
            
            if need == have:
                res.append(left)
            
            have[s[left]] -= 1
            if have[s[left]] == 0:
                del have[s[left]]
            
            left += 1
        
        return res