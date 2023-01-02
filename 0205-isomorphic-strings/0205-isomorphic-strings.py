class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()
        
        for c1, c2 in zip(s, t):
            if c1 not in mapping:
                if c2 not in mapped:
                    mapping[c1] = c2
                    mapped.add(c2)
                else:
                    return False
            elif mapping[c1] != c2:
                return False
        
        return True
            