class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = Counter(words)
        max_heap = []
        
        for word, freq in counter.items():
            heapq.heappush(max_heap, (-freq, word))
        
        top_k = heapq.nsmallest(k, max_heap)
        
        return [word for _, word in top_k]