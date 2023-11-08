# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.preorder_idx = 0
        
        def helper(left, right):
            if left > right:
                return 
            
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(root_val)
            
            idx = val_idx[root_val]
            
            # Construct left and right subtrees
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)
            return root
        
        
        val_idx = {v:i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)