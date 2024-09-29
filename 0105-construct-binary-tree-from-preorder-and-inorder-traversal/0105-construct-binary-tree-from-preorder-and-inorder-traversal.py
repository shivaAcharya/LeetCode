# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder_idx = 0
        inorder_idx = {k : v for v, k in enumerate(inorder) }
        
        def helper(left, right):
            nonlocal preorder_idx
            
            if left <= right:
                root_val = preorder[preorder_idx]
                preorder_idx += 1
                root = TreeNode(root_val)
                root.left = helper(left, inorder_idx[root_val] - 1)
                root.right = helper(inorder_idx[root_val] + 1, right)
                return root        
        
        return helper(0, len(preorder) - 1)
    