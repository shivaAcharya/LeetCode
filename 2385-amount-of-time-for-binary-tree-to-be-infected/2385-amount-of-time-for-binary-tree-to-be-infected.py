# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        G = defaultdict(list)
        
        def dfs(node):
            if node.left:
                G[node.val].append(node.left.val)
                G[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                G[node.val].append(node.right.val)
                G[node.right.val].append(node.val)
                dfs(node.right)
        
        dfs(root)
        
        
        Q = deque([(start, 0)])
        visited = set([start])
        
        while Q:
            node, minute = Q.popleft()

            for nei in G[node]:
                if nei not in visited:
                    visited.add(nei)
                    Q.append((nei, minute + 1))
        
        return minute
    