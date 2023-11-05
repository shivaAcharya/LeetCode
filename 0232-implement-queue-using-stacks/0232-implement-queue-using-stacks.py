class MyQueue:

    def __init__(self):
        self.my_q = []
        self.aux_q = []

    def push(self, x: int) -> None:
        self.my_q.append(x)

    def pop(self) -> int:
        if not self.aux_q:
            while self.my_q:
                self.aux_q.append(self.my_q.pop())
        
        return self.aux_q.pop()

    def peek(self) -> int:
        if not self.aux_q:
            while self.my_q:
                self.aux_q.append(self.my_q.pop())
        
        return self.aux_q[-1]

    def empty(self) -> bool:
        return not self.my_q and not self.aux_q


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()