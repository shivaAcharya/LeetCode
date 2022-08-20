class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.map = defaultdict(int)
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        ret = -1
        if self.stack:
            size = len(self.stack)
            ret = self.stack.pop() + self.map[size]
            self.map[size - 1] += self.map[size]
            self.map[size] = 0
        return ret
        

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            k = len(self.stack)
        self.map[k] += val
    
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)