class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        G = defaultdict(list)
        
        for u, v, w in times:
            G[u].append((w, v))
        
        visited = set()
        #total_cost = [float("inf")] * (n + 1)
        heap = [(0, k)]
        max_cost = 0
        
        while heap:
            
            cost, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            max_cost = max(max_cost, cost)
            
            visited.add(node)
            for wei, nei in G[node]:
                if nei not in visited:
                    heapq.heappush(heap, (cost + wei, nei))
        
        return max_cost if len(visited) == n else -1