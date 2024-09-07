"""
stack = [-2, 0, -3]
min_stack = [-2, -3]


"""


class MinStack:

    def __init__(self):
        self.stack, self.min_stack = [], []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        popped_elem = self.stack.pop()
        if self.min_stack and popped_elem == self.min_stack[-1]:
            self.min_stack.pop()
        return popped_elem
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()