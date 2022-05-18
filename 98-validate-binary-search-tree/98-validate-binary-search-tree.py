# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        
        def inorder(node):
            if not node:
                return True
            
            left = inorder(node.left)
            
            if self.prev is None:
                self.prev = node.val
            
            elif node.val <= self.prev:
                return False
            
            self.prev = node.val
            
            return left and inorder(node.right)
        
        return inorder(root)