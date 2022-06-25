# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(start, end):
            if start <= end:
                root_idx = (start + end) // 2
                
                root = TreeNode(nums[root_idx])
                root.left = helper(start, root_idx - 1)
                root.right = helper(root_idx + 1, end)
                
                return root
        
        return helper(0, len(nums) - 1)