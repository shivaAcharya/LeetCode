class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        '''
        Properties of a binary tree:
        1. Only one root
        2. Less than or equal to two children
        3. No cycle
        
        Approach
        1. Create a set of existing children
        2. Iterate over left and right children and check for duplicates
        
        '''
        def find_root():
            children = set(leftChild) | set(rightChild)
            
            for i in range(n):
                if i not in children:
                    return i
                
            return -1
        
        root = find_root()
        if root == -1:
            return False
        
        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    
                    stack.append(child)
                    seen.add(child)
        
        return len(seen) == n