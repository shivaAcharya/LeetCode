from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        L = len(self.sl)
        # Handle odd
        if L % 2:
            return self.sl[L // 2]
        return (self.sl[L // 2] + self.sl[L // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()