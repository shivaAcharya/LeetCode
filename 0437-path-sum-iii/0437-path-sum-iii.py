# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.count = 0
        
        def dfs(node):
            if not node: return []
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            node_val = node.val
            res = [node_val]
            if node_val == targetSum: self.count += 1
            for num in left + right:
                if node_val + num == targetSum:
                    self.count += 1
                res.append(node_val + num)
            return res
        
        dfs(root)
        return self.count