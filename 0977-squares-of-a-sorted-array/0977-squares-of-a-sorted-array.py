class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        left, right = 0, N - 1
        
        for i in range(N - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
                
            res[i] = square * square
        return res