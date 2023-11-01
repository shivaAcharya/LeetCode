# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        1. Create an empty res hashmap.
        2. Perform tree-traversal (inorder) with parent node's val.
        3. If duplicates found, populate the hashmap
        
        """
        
        self.modes = collections.defaultdict(int)
        
        def dfs(node):
            if node:
                self.modes[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        max_freq = max(self.modes.values())
        return [k for k, v in self.modes.items() if v == max_freq]