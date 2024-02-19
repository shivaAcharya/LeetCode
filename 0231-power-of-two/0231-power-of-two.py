# https://leetcode.com/problems/power-of-two/editorial/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n
    