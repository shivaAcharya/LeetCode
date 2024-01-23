class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(source):
            Q = deque([source])
            color[source] = 0 # Start by marking source as 'RED'
            
            while Q:
                node = Q.popleft()
                for nei in G[node]:
                    # If there is conflict, return False
                    if color[nei] == color[node]:
                        return False
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        Q.append(nei)
            
            return True            
            
        
        G = defaultdict(set)
        for a, b in dislikes:
            G[a].add(b)
            G[b].add(a)

        color = [-1] * (n + 1) # 0 stands for red and 1 stands for blue, -1 uncolored
        for i in range(1, n + 1):
            if color[i] == -1:
                # for each pending component, run BFS
                if not bfs(i):
                    # Return False if there is conflict in the component
                    return False
        
        return True
        