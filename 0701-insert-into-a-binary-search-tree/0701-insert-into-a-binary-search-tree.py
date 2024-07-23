# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        cur = root
        while cur:
            if cur.val < val:
                if cur.right:
                    cur = cur.right
                else:
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    break
        
        if cur.val < val:
            cur.right = TreeNode(val)
        else:
            cur.left = TreeNode(val)
            
        return root
        