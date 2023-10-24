# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        Q = [root]
        res = []
        
        if not root: return res
        res.append(root.val)
        
        while Q:         
            children = []
            max_row_value = float("-inf")
            for node in Q:
                for child in node.left, node.right:
                    if child:
                        max_row_value = max(max_row_value, child.val)
                        children.append(child)
            
            Q = children
            res.append(max_row_value)
            
        res.pop()        
        return res
    