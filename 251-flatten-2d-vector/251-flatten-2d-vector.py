class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = [x for lst in vec for x in lst]
        self.ptr = 0

    def next(self) -> int:
        self.ptr += 1
        return self.vec[self.ptr - 1]

    def hasNext(self) -> bool:
        return self.ptr < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()