# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def has_one(node):
            if not node:
                return False
            
            Q = [node]
            
            while Q:
                for node in Q:
                    if node.val == 1:
                        return True
                
                Q = [child for node in Q for child in (node.left, node.right) if child]
            
            return False
        
        Q = [root]
        
        while Q:
            for node in Q:
                if not has_one(node.left):
                    node.left = None
                if not has_one(node.right):
                    node.right = None
            
            Q = [child for node in Q for child in (node.left, node.right) if child]
        
        if root.val == 0 and not has_one(root):
            
            return 
        
        return root
        