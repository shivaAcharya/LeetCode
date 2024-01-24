# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Peform DFS with backtracking and check palindromicity with boolean array
        
        path = [False] * 10 # 0-indexed 
        self.res = 0
        
        def dfs(node):

            path[node.val] = not path[node.val]
            
            # Handle leaf nodes
            if not node.left and not node.right and sum(path) < 2:
                self.res += 1
                return
                
            
            for child in node.left, node.right:
                if child:
                    dfs(child)
                    path[child.val] = not path[child.val]
        
        
        
        dfs(root)
        return self.res