# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return res
        
        Q = [root]
        res.append([root.val])
        
        while Q:
            children = []
            node_values = []
            for node in Q:
                for child in node.left, node.right:
                    if child:
                        node_values.append(child.val)
                        children.append(child)
                        
            Q = children
            if node_values:
                res.append(node_values)
        
        return res