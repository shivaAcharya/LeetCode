# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_BST(node, lo, hi):
            if not node: return True
                
            if not lo < node.val < hi: return False

            return is_BST(node.left, lo, node.val) and is_BST(node.right, node.val, hi)
            
        
        
        return is_BST(root, float("-inf"), float("inf"))