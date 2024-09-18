from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        
        def compare(a, b):
            if a + b > b + a: return -1
            if a + b < b + a: return 1
            return 0
        
        nums_str.sort(key=cmp_to_key(compare))
        
        return '0' if nums_str[0] == '0' else "".join(nums_str)
    