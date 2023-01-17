class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = strs[0]
        
        for i in range(len(strs) - 1):
            word1, word2 = strs[i], strs[i + 1]
            
            if not word1 or not word2: return ""
            if word1[0] != word2[0]: return ""
            
            prefix = []
            for c1, c2 in zip(word1, word2):
                if c1 != c2: break
                prefix.append(c1)
            
            if len(prefix) < len(lcp):
                lcp = "".join(prefix)
        
        return lcp