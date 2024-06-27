class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        nodes = []
        for u, v in edges:
            nodes.append(u)
            nodes.append(v)
            
        counter = Counter(nodes)
        
        max_edge = max(counter.values())
        
        for node, freq in counter.items():
            if freq == max_edge:
                return node
        