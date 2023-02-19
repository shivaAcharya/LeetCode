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
        level = 0
        if not root: return res
        
        Q = [root]
        
        while Q:
            if level % 2:
                res.append([node.val for node in reversed(Q)])
            else:
                res.append([node.val for node in Q])
            children = [child for node in Q for child in (node.left, node.right) if child]
            Q = children
            level += 1
        
        return res