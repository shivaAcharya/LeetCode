class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        confusing_nums = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        str_n = str(n)
        
        rotated_num = []
        for digit in reversed(str_n):
            if digit not in confusing_nums:
                return False
            rotated_num.append(confusing_nums[digit])
        
        return int("".join(rotated_num)) != n