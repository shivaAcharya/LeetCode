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
        
        def inOrder(node, level):
            
            if node:
                
                if level > len(res):
                    res.append([])
                
                for child in node.children:
                    
                    inOrder(child, level + 1)

                res[level - 1].append(node.val)

        
        inOrder(root, 1)
        
        return res