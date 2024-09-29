# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                if len(heap) != k:
                    heapq.heappush(heap, node.val)
                else:
                    return
                inorder(node.right)
                
        inorder(root)
        return heap[-1]
        