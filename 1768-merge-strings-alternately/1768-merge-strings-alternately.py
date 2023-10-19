class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        
        for w1, w2 in zip(word1, word2):
            res.append(w1)
            res.append(w2)
        
        if len(word2) < len(word1):
            return "".join(res) + word1[len(word2):]
        elif len(word1) < len(word2):
            return "".join(res) + word2[len(word1):]
        else:
            return "".join(res)