# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.heap.append(node.val)
            self.heap = heapq.nsmallest(k, self.heap)

            inorder(node.right)
        inorder(root)
        
        return self.heap[-1]    