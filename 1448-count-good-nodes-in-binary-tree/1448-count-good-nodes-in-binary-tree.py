# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.good_nodes = 0
        
        def dfs(node, max_val):
            # Base case
            if node:
                if node.val >= max_val:
                    self.good_nodes += 1
                    max_val = node.val
                dfs(node.left, max_val)
                dfs(node.right, max_val)        
        
        
        dfs(root, float("-inf"))
        return self.good_nodes