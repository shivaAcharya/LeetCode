# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node, i):
            if not node:
                return -1
            
            if i > len(res):
                res.append([])
                                    
            left = 1 + dfs(node.left, i+1)
            right = 1 + dfs(node.right, i+1)
            
            res[max(left, right)].append(node.val)
            
            return max(left, right)
        
        dfs(root, 1)
        return res
            
            