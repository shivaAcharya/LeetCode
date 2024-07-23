# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
3 -> 0
5 -> 1
1 -> 1

"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def populate_parent_map(node, parent):
            if node:
                parent_map[node] = parent
                populate_parent_map(node.left, node)
                populate_parent_map(node.right, node)

        def get_nodes(node, num_of_nodes_away):
            if not node or node in traversed or num_of_nodes_away > k:
                return
            
            traversed.add(node)
            if num_of_nodes_away == k:
                res.append(node.val)
                return
            
            get_nodes(node.left, num_of_nodes_away + 1)
            get_nodes(node.right, num_of_nodes_away + 1)
            get_nodes(parent_map[node], num_of_nodes_away + 1)
            
        
        
        parent_map = {}
        populate_parent_map(root, None)
        traversed = set()
        res = []
        get_nodes(target, 0)
        
        return res
                
        