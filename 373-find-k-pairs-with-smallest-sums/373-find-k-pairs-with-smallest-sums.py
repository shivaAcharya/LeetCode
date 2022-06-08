class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        visited = set()
        
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        
        while len(res) < k and heap:
            
            s, l, r = heapq.heappop(heap)
            
            res.append([nums1[l], nums2[r]])
            
            if l < len(nums1) - 1 and (l + 1, r) not in visited:
                heapq.heappush(heap, (nums1[l+1] + nums2[r], l + 1, r))
                visited.add((l + 1, r))
            
            if r < len(nums2) - 1 and (l, r + 1) not in visited:
                heapq.heappush(heap, (nums1[l] + nums2[r+1], l, r + 1))
                visited.add((l, r + 1))
            
        return res