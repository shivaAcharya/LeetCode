"""
tokens = ['2', '1', '+', '3', '*']

res = 9

nums = [3]
ops = [+]

["4","13","5","/","+"]

4, 2


"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for tkn in tokens:
            # print(stack)
            if tkn not in '+-*/':
                stack.append(int(tkn))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tkn == '+':
                    stack.append(num2 + num1)
                elif tkn == '-':
                    stack.append(num2 - num1)
                elif tkn == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
        return stack.pop()

"""
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack = [0]

"""