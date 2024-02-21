# https://leetcode.com/problems/bitwise-and-of-numbers-range/editorial/
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0   
        # find the common 1-bits
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
    