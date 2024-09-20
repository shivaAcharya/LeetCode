class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 1:
            return 0
        level = 0
        while n != 1:
            if n % 2 == 0:
                n, level = n // 2, level + 1
            elif n == 3:
                n, level = n - 1, level + 1
            else:
                if ((n - 1) // 2) % 2 == 0:
                    n, level = n - 1, level + 1
                else:
                    n, level = n + 1, level + 1
        return level
        