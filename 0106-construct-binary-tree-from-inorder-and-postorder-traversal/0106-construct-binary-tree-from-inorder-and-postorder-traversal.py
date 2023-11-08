# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right:
                return
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            idx = val_idx[root_val]
            
            # Construct right and left subtrees
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            
            return root            
        
        val_idx = {v:i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)