# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_freq = defaultdict(int)
        
        def postorder(node):
            if not node:
                return [0]
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            # Process node
            total_sum = [node.val + left_sum + right_sum for left_sum in left for right_sum in right]
            
            for tot_sum in total_sum:
                sum_freq[tot_sum] += 1
            
            return total_sum
        
        postorder(root)
        res = []
        max_freq = max(sum_freq.values())
        #print(sum_freq)
        for k, v in sum_freq.items():
            if v == max_freq:
                res.append(k)
                
        return res