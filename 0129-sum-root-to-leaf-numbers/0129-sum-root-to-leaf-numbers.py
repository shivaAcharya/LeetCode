# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        self.path = [str(root.val)]
        
        def backtrack(node):
            #print(self.path)
            # Check if node is a leaf node
            if not node.left and not node.right:
                #self.path.append(str(node.val))
                self.res += int("".join(self.path))
                return

            for child in (node.left, node.right):
                if child:
                    self.path.append(str(child.val))
                    backtrack(child)
                    self.path.pop()
        
        backtrack(root)
        return self.res
                