# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)
        
        def preorder(node):
            if not node:
                return False
            
            return is_same_tree(node, subRoot) or preorder(node.left) or preorder(node.right)
        
        return preorder(root)