import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        heap = heapq.nlargest(k, nums)
        return heap[-1]
    