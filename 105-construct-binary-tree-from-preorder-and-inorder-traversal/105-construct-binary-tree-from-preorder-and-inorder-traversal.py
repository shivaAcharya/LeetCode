# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx = {node : idx for idx, node in enumerate(inorder)}
        
        self.preorder_idx = 0
        
        def helper(left, right):
            if left <= right:
                
                node_val = preorder[self.preorder_idx]
                self.preorder_idx += 1
                
                idx = inorder_idx[node_val]
                
                root = TreeNode(node_val)
                root.left = helper(left, idx - 1)
                root.right = helper(idx + 1, right)
                return root               
                
        
        return helper(0, len(inorder) - 1)