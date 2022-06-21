# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root_idx = [0] # Tracks current subtree
        
        def helper(lo, hi):
            if root_idx[0] < len(preorder):
                root_val = preorder[root_idx[0]]
                
                if not lo <= root_val <= hi:
                    return
                
                root_idx[0] += 1
                
                # The order of following two calls are critical
                root = TreeNode(root_val)
                root.left = helper(lo, root_val)
                root.right = helper(root_val, hi)
                return root
        
        return helper(float("-inf"), float("inf"))