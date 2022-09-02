# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node, parent_val, cur_length):
            
            if node:
                
                if node.val == parent_val + 1:
                    cur_length += 1
                else:
                    cur_length = 1 # Reset the length to zero
                
                self.res = max(self.res, cur_length)
                
                dfs(node.left, node.val, cur_length)
                dfs(node.right, node.val, cur_length)
        
        dfs(root, root.val, 1)
        
        return self.res
                    