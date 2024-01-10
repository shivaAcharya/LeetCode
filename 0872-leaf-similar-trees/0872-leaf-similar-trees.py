# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_nodes1, leaf_nodes2 = [], []
        
        def inorder(root, arr):
            
            if root:  
                inorder(root.left, arr)
                if not root.left and not root.right:
                    arr.append(root.val)
                inorder(root.right, arr)
                return arr
        
        return inorder(root1, []) == inorder(root2, [])
        