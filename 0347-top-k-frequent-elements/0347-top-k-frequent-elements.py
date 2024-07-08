"""
1 -> 3
2 -> 2
3 -> 1

(3, 1), (2, 2), (1, 3)


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        n_freq = heapq.nlargest(k, counter.values())
        
        return [u for u, v in counter.items() if v in n_freq]
        