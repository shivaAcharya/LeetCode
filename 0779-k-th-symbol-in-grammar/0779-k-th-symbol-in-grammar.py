# https://leetcode.com/problems/k-th-symbol-in-grammar/solution/
class Solution:
    def dfs(self, n, k, root_val):
        if n == 1:
            return root_val
        
        total_nodes = 2 ** (n - 1)
        
        # Target node will be present in the right half sub-tree of the current root node.
        if k > (total_nodes / 2):
            next_root_val = 1 if root_val == 0 else 0
            return self.dfs(n - 1, k - (total_nodes / 2), next_root_val)
        # Otherwise, the target node is in the left sub-tree of the current root node.
        else:
            next_root_val = 0 if root_val == 0 else 1
            return self.dfs(n - 1, k, next_root_val)
        
    
    def kthGrammar(self, n: int, k: int) -> int:
        return self.dfs(n, k, 0)