"""
s = ()(())
        ^    
score = 1 + 2 = 3

score = 1
stack = [3]

If open => add 0 to the stack
If close => pop, muliply by 2, add max(1, 2 * popped_elem) to stack[-1]
Return the last stack element

"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for para in s:
            if para == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(1, 2 * v)
        
        return stack[-1]
        