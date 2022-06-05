class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = 1
        min_window = nums[0]
        
        for num in nums:
            if num - min_window > k:
                res += 1
                min_window = num
        
        return res