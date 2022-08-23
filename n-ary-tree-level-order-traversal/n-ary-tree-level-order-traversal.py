"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        res = []
        
        def dfs(node, level):
            if node:
                
                if level + 1 > len(res):
                    res.append([])
                    
                for child in node.children:
                    dfs(child, level + 1)
                
                res[level].append(node.val)
        
        dfs(root, 0)
        
        return res