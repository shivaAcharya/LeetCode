# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = collections.defaultdict(list)
        res = []
        if not root:
            return res
        
        # BFS
        Q = deque([(root, 0)])
        
        while Q:
            node, col = Q.popleft()
            nodes[col].append(node.val)
            
            if node.left:
                Q.append((node.left, col - 1))
            
            if node.right:
                Q.append((node.right, col + 1))

        
        cols = sorted(nodes.keys())
        
        for col in cols:
            res.append(nodes[col])
        
        return res