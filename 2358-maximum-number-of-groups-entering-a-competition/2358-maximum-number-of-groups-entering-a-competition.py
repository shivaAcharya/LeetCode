class Solution:
    def maximumGroups(self, A: List[int]) -> int:
        n = len(A)
        k = 0
        while n > k:
            k += 1
            n -= k
        return k
                