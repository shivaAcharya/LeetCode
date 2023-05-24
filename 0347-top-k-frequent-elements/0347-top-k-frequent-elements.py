class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        top_k_freq = heapq.nlargest(k, counter.values())
                                    
        res = []
        
        for k, v in counter.items():
            if v in top_k_freq:
                res.append(k)
        
        return res