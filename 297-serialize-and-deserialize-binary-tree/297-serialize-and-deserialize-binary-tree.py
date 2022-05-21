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
            if self.idx < len(data):
                if data[self.idx] == 'N':
                    self.idx += 1
                    return None

                root = TreeNode(int(data[self.idx]))
                self.idx += 1
                root.left = build_tree()
                root.right = build_tree()
                return root
            
        return build_tree()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))