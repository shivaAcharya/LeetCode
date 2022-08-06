class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = (minutesToTest / minutesToDie)
        return math.ceil(math.log(buckets, T + 1))