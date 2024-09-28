# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        
        Q = deque([root])
        
        while Q:
            L = len(Q)
            res.append(Q[-1].val)
            
            for _ in range(L):
                node = Q.popleft()
                for child in node.left, node.right:
                    if child:
                        Q.append(child)
        
        return res                
        