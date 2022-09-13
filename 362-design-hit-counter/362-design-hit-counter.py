class HitCounter:

    def __init__(self):
        self.ls = []  # holds tuples of (timestamp, index of timestamp that was 5 mins ago)
        self.ptr = 0  # index to element that was "five minutes ago", updated on add
        

    def hit(self, timestamp: int) -> None:
        while self.ptr < len(self.ls) and self.ls[self.ptr][0] <= timestamp - 300:
            self.ptr += 1
        self.ls.append((timestamp, self.ptr))
        

    def getHits(self, timestamp: int) -> int:
        if not self.ls:
            return 0
        end_idx = bisect_right(self.ls, timestamp, key = lambda x: x[0])
        start_idx = max(self.ls[end_idx-1][1], 0)
        while start_idx < len(self.ls) and self.ls[start_idx][0] <= timestamp - 300:
            start_idx += 1
        return end_idx-start_idx


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)