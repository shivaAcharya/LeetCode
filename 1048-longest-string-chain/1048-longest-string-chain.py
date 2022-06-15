class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsPresent = set(words)
        memo = {}
        maxChainLength = 0
        def dfs(currentWord):
            if currentWord in memo:
                return memo[currentWord]
            
            maxLength = 1
            
            for i in range(len(currentWord)):
                newWord = currentWord[:i] + currentWord[i+1:]
                if newWord in wordsPresent:
                    currentLength = 1 + dfs(newWord)
                    maxLength = max(maxLength, currentLength)
            memo[currentWord] = maxLength
            return maxLength
                
        
        for word in words:
            maxChainLength = max(maxChainLength, dfs(word))
        
        return maxChainLength