# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_depth = 0
        # BFS
        Q = [root]
        
        while Q:
            max_depth += 1
            Q = [child for node in Q for child in (node.left, node.right) if child]
        
        return max_depth
                