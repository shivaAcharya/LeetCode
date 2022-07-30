class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = cur_sum = float("-inf")

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum

'''
Luna's approach
nums = [-2,1,-3,4,-1,2,1,-5,4]
max_subarray = -2
cursum = 0

for num in nums

  if cursum < 0:
    cursum = 0

  cursum += num
  max_subarray = max(max_subarray, cursum)

return max_subarray

'''