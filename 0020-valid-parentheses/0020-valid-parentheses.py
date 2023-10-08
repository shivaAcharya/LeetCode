class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        stack = []
        
        for p in s:
            if p in para:
                stack.append(para[p])
            elif not stack or stack.pop() != p:
                return False
        
        return not stack
        
        