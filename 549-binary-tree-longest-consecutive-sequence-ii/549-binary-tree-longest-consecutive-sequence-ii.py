# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.maxVal = 0
        
        def longestPath(node) -> List:
            if not node:
                return [0, 0]
                
            inr = dcr = 1
            
            if node.left:
                left = longestPath(node.left)

                if node.left.val == node.val - 1:
                    dcr = left[1] + 1

                elif node.left.val == node.val + 1:
                    inr = left[0] + 1
            
            if node.right:
                right = longestPath(node.right)
                
                if node.right.val == node.val - 1:
                    dcr = max(dcr, right[1] + 1)
                
                elif node.right.val == node.val + 1:
                    inr = max(inr, right[0] + 1)
            
            self.maxVal = max(self.maxVal, dcr + inr - 1)
            return [inr, dcr]
        
        longestPath(root)
        return self.maxVal