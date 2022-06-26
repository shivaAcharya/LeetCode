# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        Q = [root]
        
        while Q:
            max_val = float("-inf")
            tmp = []
            
            for node in Q:
                max_val = max(max_val, node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            
            res.append(max_val)
            Q = tmp
        
        return res