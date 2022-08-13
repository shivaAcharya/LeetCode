class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        '''
        pattern -> col
        text -> row
        
        if Pattern is '.' or pattern matches with text:
            copy previous match
        if pattern is "*":
            (1) eliminate the "*" and check if match in col - 2
            (2) if pattern with char preceding * and text matches, then check match in top row i.e. row - 1
        
        '''
        # https://leetcode.com/problems/regular-expression-matching/solution/     
        
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]