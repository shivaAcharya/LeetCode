"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        
        def dfs(node):
            if not node:
                return
            
            if node in mapping:
                return mapping[node]
            
            mapping[node] = Node(node.val)
            
            for nei in node.neighbors:
                mapping[node].neighbors.append(dfs(nei))
            
            return mapping[node]
            
        
        return dfs(node)