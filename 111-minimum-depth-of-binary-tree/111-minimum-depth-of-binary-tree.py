# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        Q = [(root, 1)]

        while Q:
            tmp = []
            for node, depth in Q:

                if not node.left and not node.right:
                    return depth

                if node.left:
                    tmp.append((node.left, depth + 1))

                if node.right:
                    tmp.append((node.right, depth + 1))

            Q = tmp