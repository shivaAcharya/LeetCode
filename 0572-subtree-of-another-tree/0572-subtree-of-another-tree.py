# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p, q):
            if not p and not q: 
                return True
            
            if not p or not q:
                return False
            
            return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        
        Q = deque([root])
        while Q:
            node = Q.popleft()
            
            if node.val == subRoot.val and is_same_tree(node, subRoot):
                return True
            
            for child in node.left, node.right:
                if child:
                    Q.append(child)
        
        return False
    