class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        n = len(points)
        min_cost = 0
        edges_used = 0
        in_MST = [False] * n
        heap = [(0, 0)]        
        
        
        while edges_used < n:
            cost, node = heapq.heappop(heap)
            
            if not in_MST[node]:
                in_MST[node] = True
                edges_used += 1
                min_cost += cost
                
                for next_node in range(n):
                    #if not in_MST[vertex]:
                    if not in_MST[next_node]:
                        next_cost = abs(points[node][0] - points[next_node][0]) +\
                                  abs(points[node][1] - points[next_node][1])
                        heapq.heappush(heap, (next_cost, next_node))
        
        return min_cost