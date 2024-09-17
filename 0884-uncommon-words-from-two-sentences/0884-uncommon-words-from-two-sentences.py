class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        word_counter = Counter(s1.split() + s2.split())
        res = []
        
        for word, count in word_counter.items():
            if count == 1:
                res.append(word)
                
        return res
    