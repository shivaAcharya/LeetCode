# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = [[root.val]]
        Q = deque([root])
        
        while Q:
            children = []
            children_vals = []
            for node in Q:
                for child in node.left, node.right:
                    if child:
                        children.append(child)
                        children_vals.append(child.val)
            Q = children
            if children:
                res.append(children_vals[:])
        return res
        