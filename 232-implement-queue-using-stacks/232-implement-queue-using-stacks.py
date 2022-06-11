class MyQueue:

    def __init__(self):
        self.queue, self.stack = [], []
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        if not self.stack:
            # Transfer all the elements from the queue to the stack
            while self.queue:
                self.stack.append(self.queue.pop())
        
        return self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return self.queue[0]
    
    def empty(self):
        return not (self.queue or self.stack)
        # if self.stack1 or self.stack2:
        #     return False
        # return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()