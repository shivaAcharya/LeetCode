class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        
        counter = Counter(arr)
        
        freq = sorted(counter.values(), reverse=True)
        
        for i, freq in enumerate(freq):
            
            N -= freq
            
            if N <= len(arr) / 2:
                return i + 1