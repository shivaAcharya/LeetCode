# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        Q = deque([root])
        res = []
        
        if not root: return res
        
        while Q:         
            max_row_value = float("-inf")
            
            for _ in range(len(Q)):
                node = Q.popleft()
                max_row_value = max(max_row_value, node.val)
                for child in node.left, node.right:
                    if child:
                        Q.append(child)
            
            res.append(max_row_value)
                  
        return res
    