class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize components
        components = 0
        
        # Initialize visited hashset
        visited = set()
        
        # Create adjacency list
        adj_list = {}
        for edge in edges:
            adj_list[edge[0]] = adj_list.get(edge[0], []) + [edge[1]]
            adj_list[edge[1]] = adj_list.get(edge[1], []) + [edge[0]]
        
        # Create DFS function
        def dfs(start):
            visited.add(start)
            
            for neigh in adj_list.get(start, []):
                if neigh not in visited:
                    dfs(neigh)
        
        
        # Main loop
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components