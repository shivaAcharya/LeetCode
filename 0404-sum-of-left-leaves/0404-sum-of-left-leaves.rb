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
def sum_of_left_leaves(root)
    
    $res = 0
    def dfs(node, left)
    
        if node
            if not node.left and not node.right and left
                $res += node.val
            else
                dfs(node.left, true)
                dfs(node.right, false)                
            end
        end
    end
    
    dfs(root, false)
    $res
end