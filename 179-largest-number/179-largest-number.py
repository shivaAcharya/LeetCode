from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = [str(num) for num in nums]
        
        def compare(x, y):
            if x + y > y + x: return -1
            if x + y < y + x: return 1
            return 0
        
        num_str.sort(key=cmp_to_key(compare))
        
        return "0" if num_str[0] == '0' else "".join(num_str)