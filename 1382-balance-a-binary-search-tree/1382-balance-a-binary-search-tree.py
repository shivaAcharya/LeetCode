# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # Inorder traversal
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        node_vals = inorder(root)
        
        def construct_bst(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            root_val = node_vals[mid]
            root = TreeNode(root_val)
            
            root.left = construct_bst(left, mid - 1)
            root.right = construct_bst(mid + 1, right)
            return root
        
        return construct_bst(0, len(node_vals) - 1)
        