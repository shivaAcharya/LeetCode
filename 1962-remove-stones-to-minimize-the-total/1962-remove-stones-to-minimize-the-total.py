class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        piles = [100, 10, 2], k = 6
                i = 1
            = [50, 10, 2] k = 5
            = [25, 10, 2] k = 4
            = [13, 10, 2 ] k = 3
            = [7, 10, 2] k = 2
            = [7, 5, ]
         """
        piles = [-i for i in piles]
        heapq.heapify(piles)
        """ 
        while k > 0:
            if piles[0] == -1: break
            max_element = -heapq.heappop(piles)
            max_element -= max_element // 2
            k -= 1
            heapq.heappush(piles, -max_element)
        
        return -sum(piles)
        """
        for _ in range(k):
            if piles[0] == -1: break
            heapq.heapreplace(piles, math.ceil(piles[0] // 2))
        return -sum(piles)