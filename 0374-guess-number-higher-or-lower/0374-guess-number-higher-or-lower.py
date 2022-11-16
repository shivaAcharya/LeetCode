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
        num1, num2 = (lo + hi) // 2, (lo + hi + 1) // 2
        
        while True:
            pick1, pick2 = guess(num1), guess(num2)
            
            if pick1 == 0:
                return num1
            
            if pick2 == 0:
                return num2
            
            if pick1 > 0:
                lo = num1
            elif pick1 < 0:
                hi = num1
            
            num1, num2 = (lo + hi) // 2, (lo + hi + 1) // 2
