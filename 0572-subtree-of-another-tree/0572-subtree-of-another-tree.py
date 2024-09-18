# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        def dfs(node):
            if not node: return False
            
            if node.val == subRoot.val and is_same_tree(node, subRoot): return True
            
            return dfs(node.left) or dfs(node.right)
    
        return dfs(root)
    