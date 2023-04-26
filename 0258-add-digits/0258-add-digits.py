class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        
        while len(str_num) > 1:
            res = 0
            for digit in str_num:
                res += int(digit)
            str_num = str(res)
        
        return int(str_num)