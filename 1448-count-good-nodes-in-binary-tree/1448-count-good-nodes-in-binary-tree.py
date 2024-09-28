# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.good_nodes = 0
        
        def preorder(node, max_val):
            if node:
                if node.val >= max_val:
                    max_val = node.val
                    self.good_nodes += 1
                preorder(node.left, max_val)
                preorder(node.right, max_val)
        
        preorder(root, root.val)
        return self.good_nodes
        