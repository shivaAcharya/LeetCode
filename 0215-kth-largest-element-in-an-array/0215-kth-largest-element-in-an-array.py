class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = [] #[-3, -2,]

        for num in nums:
            # print(min_heap)
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]