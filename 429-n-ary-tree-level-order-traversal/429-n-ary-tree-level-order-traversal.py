"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ############################## DFS ########################
        '''   
        res = []
        def inOrder(node, level):
            if node:
                if level > len(res):
                    res.append([])

                for child in node.children:

                    inOrder(child, level + 1)

                res[level - 1].append(node.val)

        
        inOrder(root, 1)
        
        return res
        '''
        ########################## BFS ###########################
        
        res = []
        
        if not root:
            return res
        
        Q = deque([(root, 0)])
        
        while Q:
            
            node, level = Q.popleft()
            
            if level + 1 > len(res):
                res.append([])
            
            res[level].append(node.val)
            
            for child in node.children:
                Q.append((child, level + 1))
        
        return res
        
    