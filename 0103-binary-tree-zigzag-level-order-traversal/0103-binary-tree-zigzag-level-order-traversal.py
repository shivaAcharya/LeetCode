# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ########### NAIVE APPROACH ##############
        res = []
        left = True
        if not root: return res
        
        Q = [root]
        
        while Q:
            if not left:
                res.append([node.val for node in reversed(Q)])
                left = True
            else:
                res.append([node.val for node in Q])
                left = False
            children = [child for node in Q for child in (node.left, node.right) if child]
            Q = children
        
        return res