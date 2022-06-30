# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        Q = [root]
        
        while Q:
            res.append(sum([node.val for node in Q]) / len(Q))
            Q = [child for node in Q for child in (node.left, node.right) if child]
        
        return res
    