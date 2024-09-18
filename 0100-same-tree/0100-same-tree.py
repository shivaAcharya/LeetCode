# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both null, return True
        if not p and not q: return True        
        
        # If one of the nodes is null, return False
        if not p or not q: return False
        
        # If the values of two nodes are different, return False        
        # Recursively check the left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    