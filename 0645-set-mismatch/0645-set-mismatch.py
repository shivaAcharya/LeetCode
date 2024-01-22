"""
nums = [1, 2, 2, 3]

"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = [0, 0] #[dups, missing]
        
        for num in range(1, len(nums) + 1):
            if num not in counter:
                res[1] = num
            
            if counter[num] > 1:
                res[0] = num
        
        return res
        