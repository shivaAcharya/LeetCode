class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = set([(i+1) for i in range(1100)])

    def popSmallest(self) -> int:
        ret = min(self.smallest)
        self.smallest.remove(ret)
        return ret

    def addBack(self, num: int) -> None:
        self.smallest.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)