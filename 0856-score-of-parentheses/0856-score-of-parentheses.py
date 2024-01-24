"""
Initiate stack with score 0
Iterate over s
    For (, add 0 in stack
    For ), pop the stack and add max(stack.pop() * 2, 1) to stack.peek
Return stack.pop()

"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for para in s:
            if para == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(v * 2, 1)
            # print(stack)
        return stack.pop()
    