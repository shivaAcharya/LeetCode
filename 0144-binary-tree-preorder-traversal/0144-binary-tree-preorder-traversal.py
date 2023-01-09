# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
                1
            2      5
        3     4  6    7
        
        res = [1, 2, 3, 4, 5, 6, 7]
        stack = [5, 4]
        
        '''
        
        if not root: return []
        
        res, stack = [], [root]
        
        while stack:
            
            node = stack.pop()
            
            while node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
        
        return res
            
            
            