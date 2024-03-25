"""
        0  1  2  3 4  5  6  7
nums = [4,3,2,7,8,2,3,1]
res = [2, 3]


"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # nums.append(0)
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        
        return res
        