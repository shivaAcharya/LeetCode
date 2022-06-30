class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """

        numberOfMoves_k = [(k ∗ countBefore_k)−(sumBefore_k)]+[(sumAfter_k)−(k ∗ countAfter_k)]

        """
        nums.sort()
        total = sum(nums)
        sumBefore, sumAfter = 0, total
        moves = float("inf")

        for i, num in enumerate(nums):
            moves = min(moves, num * i - sumBefore + sumAfter - num * (len(nums) - i))
            sumBefore += num
            sumAfter -= num

        return moves

        
    