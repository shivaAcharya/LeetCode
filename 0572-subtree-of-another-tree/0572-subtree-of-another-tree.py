# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p, q):
            # Return True if both null
            if not p and not q: return True
            
            # Return False if one tree is null
            if not p or not q: return False
            
            if p.val != q.val: return False
            
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        def dfs(root):
            if root:
                if root.val == subRoot.val and is_same_tree(root, subRoot):
                    return True
                return dfs(root.left) or dfs(root.right)
        
        return dfs(root)