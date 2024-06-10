class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = defaultdict(list)
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            mapping[sorted_word].append(word)
            
        return mapping.values()
        