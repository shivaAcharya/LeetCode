class MinStack:

    def __init__(self):
        self.stack, self.auxStack = [], []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.auxStack or val < self.auxStack[-1][0]:
            self.auxStack.append([val, 1])
        elif val == self.auxStack[-1][0]:
            self.auxStack[-1][-1] += 1   

    def pop(self) -> None:
        popped_item = self.stack.pop()
        if popped_item == self.auxStack[-1][0]:
            self.auxStack[-1][1] -= 1
            if not self.auxStack[-1][1]:
                self.auxStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.auxStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()