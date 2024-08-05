class Solution:
    def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
    
#         f_0, f_1 = 0, 1

#         for _ in range(2, n):
#             f_0, f_1 = f_1, f_0 + f_1

#         return f_0 + f_1

###### RECURSION WITH MEMOIZATION #######
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            if i == 1:
                return 1
            
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        return dp(n)
    