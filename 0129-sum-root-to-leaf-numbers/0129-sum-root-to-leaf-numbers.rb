# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def sum_numbers(root)
    $res = 0
    
    def dfs(node, cur_sum)
        if not node.left and not node.right
            cur_sum = cur_sum * 10 + node.val
            $res += cur_sum
        end
        
        if node.left
            dfs(node.left, cur_sum * 10 + node.val)
        end
        
        if node.right
            dfs(node.right, cur_sum * 10 + node.val)
        end    
    end
    
    dfs(root, 0)
    $res
    
end