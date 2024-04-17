# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val = val, left = root)
            
        Q = deque([root])
        
        while Q and depth > 2:
            Q = [child for node in Q for child in (node.left, node.right) if child]
            depth -= 1
        
        for node in Q:
            node.left = TreeNode(val, left = node.left)
            node.right = TreeNode(val, right = node.right)
        
        return root
    