"""
nums = [1, 2, 3, 4]
        ^ 
prod = [24, 12, 8, 6]

right_prod = 1 * 4 = 4 * 3 = 12 * 2 = 24

left_prefix =  [1, 1, 2, 6]
right_prefix = [24, 12, 4, 1]

res = [24, 12, 8. 6]

what if the array is empty? => return an empty array
if the array contains one 0 =>
if the array contains two 0s => return an array with all 0s



"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = [1] * L
        
        # Left traversal
        for i in range(1, L):
            res[i] = res[i - 1] * nums[i - 1]
        
        # Right traversal
        prod = 1
        for i in range(L - 2, -1, -1):
            prod *= nums[i + 1]
            res[i] *= prod
        
        return res

"""
nums = [1, 2, 3, 4]
           ^
L = 4
res = [24, 12, 8, 6]
# Left
1 -> 3

# Right
prod = 12
i => 2 -> 0



"""