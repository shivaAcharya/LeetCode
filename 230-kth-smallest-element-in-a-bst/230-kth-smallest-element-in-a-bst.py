# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.q = []
        def inorder(node):
            if node:
                inorder(node.left)
                self.q.append(node.val)
                self.q = heapq.nsmallest(k, self.q)
                inorder(node.right)
        
        inorder(root)
        print(self.q)
        return self.q[-1]
