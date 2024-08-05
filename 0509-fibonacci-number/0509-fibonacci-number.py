class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
    
        f_0, f_1 = 0, 1

        for _ in range(2, n):
            f_0, f_1 = f_1, f_0 + f_1

        return f_0 + f_1