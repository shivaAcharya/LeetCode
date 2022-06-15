class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        max_heap, res = [], []
        
        for char, freq in counter.items():
            heapq.heappush(max_heap, (-freq, char))
        
        for _ in range(len(max_heap)):
            freq, char = heapq.heappop(max_heap)
            res.append(char * (-freq))
        
        return "".join(res)