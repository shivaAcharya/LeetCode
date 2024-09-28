# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def preorder(node, min_val, max_val):
            if node:
                if not min_val < node.val < max_val:
                    return False
                
                return preorder(node.left, min_val, node.val) and preorder(node.right, node.val, max_val)
            return True
        
        return preorder(root, float("-inf"), float("inf"))
    
                