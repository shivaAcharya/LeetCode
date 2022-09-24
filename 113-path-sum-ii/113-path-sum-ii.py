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
                
                # If leaf node
                if not node.left and not node.right and cur_sum == targetSum:
                    res.append(path.copy())
                    return
                
                for nei in (node.left, node.right):
                    if nei:
                        path.append(nei.val)
                        cur_sum += nei.val
                        dfs(nei, cur_sum, path)
                        cur_sum -= nei.val
                        path.pop()
        
        
        dfs(root, root.val, [root.val])
        return res