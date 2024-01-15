class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        stack, cur_num, operator, L = [], 0, '+', len(s)
        
        for i, c in enumerate(s):
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            
            if not c.isdigit() and c != ' ' or i == L - 1:
                if operator == '+':
                    stack.append(cur_num)
                elif operator == '-':
                    stack.append(-cur_num)
                elif operator == '*':
                    stack.append(stack.pop() * cur_num)
                else:
                    stack.append(int(stack.pop() / cur_num))
                
                operator, cur_num = c, 0
        
        res = 0
        while stack:
            res += stack.pop()
        
        return res
        