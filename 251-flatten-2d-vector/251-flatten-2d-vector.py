class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.x = self.y = 0
        self.nxt = None
        
        for i, arr in enumerate(self.vec):
            if arr:
                self.nxt = arr[0]
                self.x = i
                break
        print(self.vec, self.x, self.nxt)

    def next(self) -> int:
        if len(self.vec[self.x]) == self.y + 1:
            self.y = 0
            self.x += 1
            while self.x < len(self.vec) and not self.vec[self.x]:
                self.x += 1 
        else:
            self.y += 1
        ret = self.nxt
        
        if self.hasNext():
            self.nxt = self.vec[self.x][self.y]
        return ret

    def hasNext(self) -> bool:
        return self.nxt != None and self.x < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()