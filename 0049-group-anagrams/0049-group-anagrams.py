from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for st in strs:
            sorted_str = "".join(sorted(st))
            groups[sorted_str].append(st)
        
        return groups.values()
        