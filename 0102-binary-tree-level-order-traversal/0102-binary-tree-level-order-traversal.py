# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        Q = deque([root])
        
        while Q:
            L = len(Q)
            node_vals = []
            for _ in range(L):
                node = Q.popleft()
                if node:
                    node_vals.append(node.val)
                    Q.append(node.left)
                    Q.append(node.right)
                        
            if node_vals:
                res.append(node_vals)
        
        return res
        