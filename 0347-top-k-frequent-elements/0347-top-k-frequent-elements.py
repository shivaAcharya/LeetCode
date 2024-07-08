"""
1 -> 3
2 -> 2
3 -> 1

(3, 1), (2, 2), (1, 3)


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        heap = []
        
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            
        n_freq = heapq.nlargest(k, heap)
        
        return [v for _, v in n_freq]
        