# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flattenTree(node):
            
            if node:
                
                # Return node if its a leaf node
                if not node.left and not node.right:
                    return node
                
                # Get left and right tail
                leftTail = flattenTree(node.left)
                rightTail = flattenTree(node.right)
                
                # Combine
                if leftTail:
                    leftTail.right = node.right
                    node.right = node.left
                    node.left = None
                
                return rightTail or leftTail
            
        flattenTree(root)