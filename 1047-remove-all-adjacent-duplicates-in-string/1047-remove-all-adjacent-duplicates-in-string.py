class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = list(s)
        
        while len(stack) != len(s):
            
            
            for c in s:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    stack.append(c)
            
            s = stack
        
        return "".join(stack)
        