# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node: return "covered"
            
            left, right = dfs(node.left), dfs(node.right)
            if left == "to_be_covered" or right == "to_be_covered":
                self.res += 1
                return "covering"
            
            return "covered" if left == "covering" or right == "covering" else "to_be_covered"
        
        return (dfs(root) == "to_be_covered") + self.res  