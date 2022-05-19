# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
         # Check if is same tree
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        # Traverse root tree
        def preorder(node):
            if not node:
                return False

            return isSameTree(node, subRoot) or preorder(node.left) or preorder(node.right)

        return preorder(root)   