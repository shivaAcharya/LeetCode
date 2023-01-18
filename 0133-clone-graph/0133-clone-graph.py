"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(node):
            if not node: return

            if node in old_to_new: return old_to_new[node]

            # Make a copy
            copy_node = Node(node.val)
            old_to_new[node] = copy_node

            # Traverse neigbors
            for nei in node.neighbors:
                copy_node.neighbors.append(dfs(nei))

            return copy_node
        
        return dfs(node)