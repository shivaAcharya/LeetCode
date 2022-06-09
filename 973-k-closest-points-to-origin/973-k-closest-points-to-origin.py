class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            heap.append((math.sqrt(x**2 + y**2), x, y))
        
        heap = heapq.nsmallest(k, heap)
        
        for _, x, y in heap:
            res.append([x, y])
        
        return res