"""
missing = 9
 0 1 2 3 4 5 6 7 8
[9,6,4,2,3,5,7,0,1]
[9,7,4,2,3,5,6,0,1]



[0,1,4,2,3,5,6,7,1]

sum_upto_n = n * (n + 1) / 2 = 6
sum_nums = 4
return sum_upto_n - sum_nums => 2
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sum_upto_n = N * (N + 1) // 2
        sum_nums = sum(nums)
        
        return sum_upto_n - sum_nums
        