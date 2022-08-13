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
                
        
        dp = [[False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
        
        dp[0][0] = True
        
        # Populate first dp row
        for col in range(2, len(pattern) + 1):
            if pattern[col - 1] == "*":
                dp[0][col] = dp[0][col - 2]
                
        # Populate dp table      
        for row in range(1, len(text) + 1):
            for col in range(1, len(pattern) + 1):
                if pattern[col - 1] == text[row - 1] or pattern[col-1] == ".":
                    dp[row][col] = dp[row - 1][col-1]
                elif pattern[col-1] == '*':
                    dp[row][col] = dp[row][col-2]
                    if pattern[col-2] == text[row-1] or pattern[col-2] == '.':
                        dp[row][col] = dp[row][col] or dp[row-1][col]
                    
        
        return dp[len(text)][len(pattern)]