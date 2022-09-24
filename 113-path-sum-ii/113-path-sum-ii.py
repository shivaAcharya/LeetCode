# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        if not root: return res
        
        def dfs(node, cur_sum, path):
            
            if node:
                
                path.append(node.val)
                
                # If leaf node
                if not node.left and not node.right and node.val == cur_sum:
                    res.append(path.copy())
                else:
                
                    dfs(node.left, cur_sum - node.val, path)
                    dfs(node.right, cur_sum - node.val, path)

                path.pop()
                
        
        dfs(root, targetSum, [])
        return res