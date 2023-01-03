# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check_symmetric(root1, root2):
            
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            
            return check_symmetric(root1.left, root2.right) and check_symmetric(root1.right, root2.left)
        
        return not root or check_symmetric(root.left, root.right)