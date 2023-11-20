class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l, r = 0, len(nums) - 1
        
        squares = [0] * len(nums)
        write_idx = len(nums) - 1
        
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                squares[write_idx] = nums[r] * nums[r]
                r -= 1
            else:
                squares[write_idx] = nums[l] * nums[l]
                l += 1
            write_idx -= 1
        
        return squares
    