class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = "+-*/"
        
        for token in tokens:
            if token in operators:
                operand1 = operands.pop()
                operand2 = operands.pop()
                
                if token == '+':
                    operands.append(operand2 + operand1)
                elif token == '-':
                    operands.append(operand2 - operand1)
                elif token == '*':
                    operands.append(operand2 * operand1)
                else:
                    result = abs(operand2) // abs(operand1)
                    operands.append(result)
                    if operand2 * operand1 < 0:
                        operands[-1] *= -1
            else:
                operands.append(int(token))
        
        return operands.pop()
        