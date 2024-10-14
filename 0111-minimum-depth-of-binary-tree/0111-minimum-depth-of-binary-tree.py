"""
Understand:
        2
     N     3
         N    4
            N    5
                N  6
                
1. Is the tree a complete tree? => No
2. Can we expect the tree to be empty? => Yes


Match:
Tree Traversal? DFS or BFS

Plan:
Post order traversal
Recursively check the minimun height from a node
 If both children are present, check min between paths
 If single child, check depth of child
 If leaf node, return it's height.

Implement:
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0
        
        # Recursively check the minimum height from a node
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.right:
            return self.minDepth(root.right) + 1
        elif root.left:
            return self.minDepth(root.left) + 1
        else: # leaf node
            return 1

"""
Review:
Dry Run

Evaluate:
Time Complexity => O(N)
Space Complexity => O(N)

"""
        