class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        res = []
        for word in words:
            mapping = {}
            seen = set()
            for i, j in zip(word, pattern):
                if i not in mapping and j not in seen:
                    mapping[i] = j
                    seen.add(j)
                elif j in seen and (i not in mapping or mapping[i] != j):
                    break
                elif mapping[i] != j:
                    break
            else:
                res.append(word)
        
        return res

                
                
                    