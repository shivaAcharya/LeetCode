import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        
        for x, y in points:
            heapq.heappush(max_heap, (- (x**2 + y**2), x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        res = []
        
        for _, x, y in max_heap:
            res.append([x, y])
        
        return res
            