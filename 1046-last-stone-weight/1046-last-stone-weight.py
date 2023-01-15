class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            
            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)
        
        return abs(stones[0]) if stones else 0