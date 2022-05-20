# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Make p the lowest
        if q.val < p.val:
            p, q = q, p
        
        ############# RECURSIVE APPROACH #######################
        """
        def lca(root, p, q):
            if not root:
                return None
            
            # If root's value is inbetween p and q, return root
            if p.val < root.val < q.val:
                return root
            
            if root is p or root is q:
                return root
            
            return lca(root.left, p, q) or lca(root.right, p, q)
        
        return lca(root, p, q)
        """
        ################# ITERATIVE APPROACH ########################
        
        while root:
            if p.val < root.val < q.val:
                return root
            
            if root is p or root is q:
                return root
            
            if root.val < p.val:
                root = root.right
            else:
                root = root.left
        
        