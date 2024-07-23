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

        Q = deque([root, None])
        node_vals = []
        
        while Q:            
            node = Q.popleft()
            # print(node, Q, res)
            if node:
                node_vals.append(node.val)
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
            else:
                res.append(node_vals[:])
                node_vals.clear()
                if Q: Q.append(None)

        return res
    