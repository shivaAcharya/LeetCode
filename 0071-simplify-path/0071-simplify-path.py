class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')
        
        stack = []
        
        for elem in path:
            if elem == '..':
                if stack:
                    stack.pop()
            elif elem and elem != '.':
                stack.append(elem)
        
        return '/' + '/'.join(stack)