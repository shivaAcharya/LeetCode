# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        heap = []
        
        def dfs(c, r, node):
            
            if node:
                # Pre-order
                heapq.heappush(heap, (c, r, node.val))
                dfs(c - 1, r + 1, node.left)
                dfs(c + 1, r + 1, node.right)            
            
        
        dfs(0, 0, root)
        res = []
        
        #print(heap)
        prev_col = None
        while heap:
            
            c, r, node_val = heapq.heappop(heap)
            
            if res and prev_col == c:
                res[-1].append(node_val)
            else:
                res.append([node_val])
            
            prev_col = c
                
        return res
        