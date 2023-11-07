# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check_symmetry(root1, root2):
            
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            return (root1.val == root2.val) and check_symmetry(root1.left, root2.right) and check_symmetry(root1.right, root2.left)
        
        return check_symmetry(root.left, root.right)
    