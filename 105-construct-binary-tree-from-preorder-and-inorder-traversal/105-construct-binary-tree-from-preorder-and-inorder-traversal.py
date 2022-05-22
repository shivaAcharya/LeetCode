# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_idx = {val : idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def construct_tree(left, right):
            if left <= right:
                val = preorder[self.preorder_idx]
                self.preorder_idx += 1
                idx = val_idx[val]
                
                root = TreeNode(val)
                root.left = construct_tree(left, idx - 1)
                root.right = construct_tree(idx + 1, right)
                return root
        
        return construct_tree(0, len(inorder) - 1)
                
                