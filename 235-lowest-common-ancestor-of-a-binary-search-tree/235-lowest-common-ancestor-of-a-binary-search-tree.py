# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            if p.val < root.val < q.val:
                return root
            if q.val < root.val < p.val:
                return root
            if root.val == p.val or root.val == q.val:
                return root
            if p.val > root.val and q.val > root.val:
                root = root.right
            else:
                root = root.left