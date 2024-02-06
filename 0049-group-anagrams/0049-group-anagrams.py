from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for word in strs:
            groups[tuple(sorted(word))].append(word)
            
        res = []
        for lst in groups.values():
            res.append(lst)
        
        return res
        