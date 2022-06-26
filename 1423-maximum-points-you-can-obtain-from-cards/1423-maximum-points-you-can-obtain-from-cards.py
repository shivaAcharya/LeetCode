class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        1. Find minimum sum subarray of length len(cardPoints) - k.
        2. Subtract minimum sum from sum(cardPoints) and return it.
        
        """
        L = len(cardPoints)
        win_size = L - k
         
        min_sum = float("inf")
        
        l, r = 0, win_size
        cur_sum = sum(cardPoints[l:r])
        min_sum = min(min_sum, cur_sum)
        
        while r < L:
            cur_sum += cardPoints[r]
            cur_sum -= cardPoints[l]
            min_sum = min(min_sum, cur_sum)
            l += 1
            r += 1
        
        return sum(cardPoints) - min_sum
        
"""
Time complexity: O(n). In the problem, we are iterating over the array of cards twice. So the time complexity will be O(2⋅n) = O(n).

Space complexity: O(1) since no extra space is required.

"""
        