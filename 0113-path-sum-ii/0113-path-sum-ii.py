# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # Base case
        if not root:
            return []
        
        self.paths = []
        self.cur_path = []
        
        def dfs(node, cur_sum):
            # If leaf node:
            if not node.left and not node.right:
                if node.val == cur_sum:
                    self.cur_path.append(node.val)
                    self.paths.append(self.cur_path[:])
                    return
            self.cur_path.append(node.val)
            cur_sum -= node.val
            for child in node.left, node.right:
                if child:
                    dfs(child, cur_sum)
                    self.cur_path.pop()
        
        dfs(root, targetSum)
        return self.paths
    