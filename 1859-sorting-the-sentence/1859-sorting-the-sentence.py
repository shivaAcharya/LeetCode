class Solution:
    def sortSentence(self, s: str) -> str:
        # Split s with space delimiter
        s = s.split()
        res = [''] * len(s)
        
        for word in s:
            res[int(word[-1]) - 1] = word[:-1]
        
        return " ".join(res)