# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        self.path = []
        
        def backtrack(node):
            #print(self.path)
            if not node:
                return
            
            self.path.append(str(node.val))
            
            # Check if node is a leaf node
            if not node.left and not node.right:
                self.res += int("".join(self.path))

            for child in (node.left, node.right):
                backtrack(child)
            self.path.pop()
        
        backtrack(root)
        return self.res
                