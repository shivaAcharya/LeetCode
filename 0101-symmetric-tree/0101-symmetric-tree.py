# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        nodes = [root]
        
        while nodes:
            # Check symmetricity and traverse children
            l, r = 0, len(nodes) - 1
            children = []            
            while l < r:
                if not nodes[l] and not nodes[r]: pass
                elif not nodes[l] or not nodes[r]: return False
                elif nodes[l].val != nodes[r].val: return False
                l += 1
                r -= 1
            
            # Populate nodes with children
            for node in nodes:
                if node:
                    children.append(node.left)
                    children.append(node.right)
            nodes = children
        
        return True
        