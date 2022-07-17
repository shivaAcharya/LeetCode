class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        def is_lcm(n, nums):
            
            for num in nums:
                if num % n:
                    return False
            
            return True
        
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if is_lcm(num, numsDivide):
                return i
        
        return -1