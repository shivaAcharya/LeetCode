# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def preorder(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return '#'.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split('#')
        self.idx = 0
        
        def build_tree():
            node_val = data[self.idx]

            if node_val == 'N':
                self.idx += 1
                return

            root = TreeNode(int(node_val))
            self.idx += 1
            root.left = build_tree()
            root.right = build_tree()
            return root
        return build_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))