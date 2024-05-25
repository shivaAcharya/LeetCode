class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parantheses = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        
        for para in s:
            if para in parantheses:
                stack.append(parantheses[para])
            elif not stack or stack.pop() != para:
                return False
        
        return not stack
        