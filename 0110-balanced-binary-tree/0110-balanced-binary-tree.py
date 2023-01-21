# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(tree):
            if not tree:
                return -1
            return 1 + max(get_height(tree.left), get_height(tree.right))
        
        def check_balance(root):
            if not root:
                return True
            
            if not abs(get_height(root.left) - get_height(root.right)) <= 1:
                return False
            
            return check_balance(root.left) and check_balance(root.right)
            
            
        return check_balance(root)
            