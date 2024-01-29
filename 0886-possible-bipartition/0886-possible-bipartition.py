class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(source):
            Q = deque([source])
            colors[source] = 0 # Start with Red
            
            while Q:
                node = Q.popleft()
                for nei in G[node]:
                    if colors[nei] == colors[node]:
                        return False
                    if colors[nei] == -1:
                        colors[nei] = 1 - colors[node]
                        Q.append(nei)
            return True
        
        
        G = defaultdict(set)
        for a, b in dislikes:
            G[a].add(b)
            G[b].add(a)
            
        colors = [-1] * (n + 1) # 0 -> RED, 1 -> BLUE, -1 -> UNCOLORED
        for i in range(1, n + 1):
            if colors[i] == -1 and not bfs(i):
                return False
        
        return True
        