# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n
        
        lo, hi = 1, n
        num = (lo + hi) // 2
        
        while True:
            pick = guess(num)
            
            if pick == 0:
                return num
            
            if pick > 0:
                lo = num + 1
            elif pick < 0:
                hi = num - 1
            
            num = (lo + hi) // 2
