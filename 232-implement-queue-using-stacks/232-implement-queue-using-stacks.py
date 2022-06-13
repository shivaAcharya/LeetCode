class MyQueue:

    def __init__(self):
        self.queue = []
        self.aux_stack = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.aux_stack:
            while self.queue:
                self.aux_stack.append(self.queue.pop())
        
        return self.aux_stack.pop()

    def peek(self) -> int:
        if not self.aux_stack:
            while self.queue:
                self.aux_stack.append(self.queue.pop())
        
        return self.aux_stack[-1]

    def empty(self) -> bool:
        return not (self.queue or self.aux_stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()