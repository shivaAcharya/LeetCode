# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_idx = {val : idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def build_tree(left, right):
            nonlocal preorder_idx
            if left <= right:
                val = preorder[preorder_idx]
                preorder_idx += 1
                idx = val_idx[val]

                root = TreeNode(val)

                root.left = build_tree(left, idx - 1)
                root.right = build_tree(idx + 1, right)
                return root

        return build_tree(0, len(inorder) - 1)