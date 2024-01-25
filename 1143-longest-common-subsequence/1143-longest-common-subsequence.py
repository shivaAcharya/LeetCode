from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    max_so_far = dp[i + 1][j + 1]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[M][N]


        '''
        ################ TOP-DOWN WITH MEMOIZATION #####################
        @lru_cache(maxsize=None)
        def dp(text1, text2):
            if not text1 or not text2: return 0

            letter1 = text1[0]
            idx2 = text2.find(letter1)

            case1 = dp(text1[1:], text2)
            case2 = 0
            if idx2 != -1:
                case2 = 1 + dp(text1[1:], text2[idx2 + 1:])

            return max(case1, case2)
        
        return dp(text1, text2)
        '''