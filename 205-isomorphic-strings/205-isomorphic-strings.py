class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()

        for a, b in zip(s, t):
            if a in mapping:
                if mapping[a] != b:
                    return False
                else:
                    continue
            
            if b in mapped:
                return False
            mapping[a] = b
            mapped.add(b)

        return True         