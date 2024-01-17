class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counter = Counter(arr)
        
        return len(list(counter.values())) == len(set(counter.values()))
    