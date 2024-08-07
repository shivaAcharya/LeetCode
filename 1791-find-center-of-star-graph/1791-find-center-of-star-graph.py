class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_count = defaultdict(int)

        for u, v in edges:
            edge_count[u] += 1
            edge_count[v] += 1
                
        for node, edge in edge_count.items():
            if edge == len(edges):
                return node
            