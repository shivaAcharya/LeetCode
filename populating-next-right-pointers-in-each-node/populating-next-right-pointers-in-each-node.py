"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return 
        
        Q = [root]
        
        while Q:
            
            for i in range(len(Q)):
                
                if i + 1 < len(Q):
                    Q[i].next = Q[i+1]
                else:
                    Q[i].next = None
            
            Q = [child for node in Q for child in (node.left, node.right) if child]
        
        return root