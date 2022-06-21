# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check_symmetric(tree):
            l, r = 0, len(tree) - 1
            while l < r:
                if not tree[l] and not tree[r]:
                    l += 1
                    r -= 1
                elif not tree[l] or not tree[r]:
                    return False
                elif tree[l].val != tree[r].val:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        Q = [root]        
    
        while Q:
            if not check_symmetric(Q):
                return False
            Q = [child for node in Q if node for child in (node.left, node.right)]
            # tmp = []
            # for node in Q:
            #     if node:
            #         tmp.append(node.left)
            #         tmp.append(node.right)
            # Q = tmp
        return True
            