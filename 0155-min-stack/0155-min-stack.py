class MinStack:

    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.aux_stack:
            self.aux_stack.append([val, 1])
        elif self.aux_stack[-1][0] >= val:
            if self.aux_stack[-1][0] == val:
                self.aux_stack[-1][1] += 1
            else:
                self.aux_stack.append([val, 1])

    def pop(self) -> None:
        ret_val = self.stack.pop()
        if ret_val == self.aux_stack[-1][0]:
            self.aux_stack[-1][1] -= 1
            if self.aux_stack[-1][1] == 0:
                self.aux_stack.pop()
        return ret_val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()